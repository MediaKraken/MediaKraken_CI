'''
  Copyright (C) 2021 Quinn D Granfor <spootdev@gmail.com>

  This program is free software; you can redistribute it and/or
  modify it under the terms of the GNU General Public License
  version 2, as published by the Free Software Foundation.

  This program is distributed in the hope that it will be useful, but
  WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
  General Public License version 2 for more details.

  You should have received a copy of the GNU General Public License
  version 2 along with this program; if not, write to the Free
  Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
  MA 02110-1301, USA.
'''

# must login to docker hub first *IF* one wants to push to dockerhub
# docker login --username=mediakraken

import argparse
import os
import shlex
import subprocess
import sys
from shutil import copyfile

from dotenv import load_dotenv

from common import common_docker_images
from common import common_network_email

# TODO proxy docker build -t mediakraken/mkbase38py3 --build-arg http_proxy="http://proxyip:8080"
#  --build-arg ALPMIRROR=dl-cdn.alpinelinux.org --build-arg PIPMIRROR=pypi.python.org .

parser = argparse.ArgumentParser(description='This program build and deploys MediaKraken')
parser.add_argument('-b', '--base', required=False,
                    help='Base images only', action="store_true")
# set args.image variable if entered - ex. ComposeMediaKrakenBaseFFMPEG
parser.add_argument('-i', '--image', metavar='image', required=False,
                    help='Image to build')
parser.add_argument('-r', '--rebuild', required=False,
                    help='Force rebuild with no cached layers', action="store_true")
parser.add_argument('-s', '--security', required=False,
                    help='Build security images', action="store_true")
parser.add_argument('-t', '--testing', required=False,
                    help='Build testing images', action="store_true")
parser.add_argument('-v', '--version', metavar='version', required=False,
                    help='The build version dev/prod/rust')
args = parser.parse_args()

# load .env stats
load_dotenv()

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', args)


def build_email_push(build_group, email_subject, branch_tag, push_hub_image=False):
    if args.rebuild:
        docker_no_cache = '--pull --no-cache'  # include pull to force update to new image
    else:
        docker_no_cache = ''
    for docker_images in build_group:
        if args.image is None or (args.image is not None and docker_images == args.image):
            # do the actual build process for docker image
            try:
                # catch images that are in a testing branch that might not exist
                if args.testing or args.security:
                    os.chdir(os.path.join(CWD_HOME_DIRECTORY,
                                          'MediaKraken_CI/docker',
                                          docker_images))
                else:
                    os.chdir(os.path.join(CWD_HOME_DIRECTORY,
                                          'MediaKraken_Deployment/docker',
                                          build_group[docker_images][2],
                                          docker_images))
            except FileNotFoundError:
                continue
            # TODO check for errors/warnings and stop if found
            # Successfully tagged
            # Let the mirror's be passed, if not used it will just throw a warning
            pid_build_proc = subprocess.Popen(shlex.split('docker build %s'
                                                          ' -t mediakraken/%s:%s'
                                                          ' --build-arg BRANCHTAG=%s'
                                                          ' --build-arg ALPMIRROR=%s'
                                                          ' --build-arg DEBMIRROR=%s'
                                                          ' --build-arg PIPMIRROR=%s .' %
                                                          (docker_no_cache,
                                                           build_group[docker_images][0],
                                                           branch_tag, branch_tag,
                                                           common_docker_images.ALPINE_MIRROR,
                                                           common_docker_images.DEBIAN_MIRROR,
                                                           common_docker_images.PYPI_MIRROR)),
                                              stdout=subprocess.PIPE, shell=False)
            email_body = ''
            while True:
                line = pid_build_proc.stdout.readline()
                if not line:
                    break
                email_body += line.decode("utf-8")
                print(line.rstrip(), flush=True)
            pid_build_proc.wait()
            subject_text = ' FAILED'
            if email_body.find('Successfully tagged mediakraken') != -1:
                subject_text = ' SUCCESS'
                # tag for local repo
                pid_tag_proc = subprocess.Popen(
                    shlex.split('docker tag mediakraken/%s:%s %s/mediakraken/%s:%s'
                                % (build_group[docker_images][0],
                                   branch_tag,
                                   common_docker_images.DOCKER_REPOSITORY,
                                   build_group[docker_images][0],
                                   branch_tag)),
                    stdout=subprocess.PIPE, shell=False)
                while True:
                    line = pid_tag_proc.stdout.readline()
                    if not line:
                        break
                    print(line.rstrip(), flush=True)
                pid_tag_proc.wait()
                # push to local repo
                pid_push_proc = subprocess.Popen(
                    shlex.split('docker push %s/mediakraken/%s:%s'
                                % (common_docker_images.DOCKER_REPOSITORY,
                                   build_group[docker_images][0],
                                   branch_tag)),
                    stdout=subprocess.PIPE, shell=False)
                while True:
                    line = pid_push_proc.stdout.readline()
                    if not line:
                        break
                    print(line.rstrip(), flush=True)
                pid_push_proc.wait()
                # push to remote repo
                if push_hub_image:
                    pid_push_proc = subprocess.Popen(
                        shlex.split('docker push mediakraken/%s:%s'
                                    % (build_group[docker_images][0],
                                       branch_tag)),
                        stdout=subprocess.PIPE, shell=False)
                    while True:
                        line = pid_push_proc.stdout.readline()
                        if not line:
                            break
                        print(line.rstrip(), flush=True)
                    pid_push_proc.wait()
            # send success/fail email
            common_network_email.com_net_send_email(os.environ['MAILUSER'],
                                                    os.environ['MAILPASS'],
                                                    os.environ['MAILUSER'],
                                                    email_subject
                                                    + build_stages[docker_images][0]
                                                    + subject_text,
                                                    email_body,
                                                    smtp_server=os.environ['MAILSERVER'],
                                                    smtp_port=os.environ['MAILPORT'])


# start
CWD_HOME_DIRECTORY = os.getcwd().rsplit('MediaKraken_CI', 1)[0]
# grab version to build via git branch
pid_git_proc = subprocess.Popen(
    shlex.split('git branch'), stdout=subprocess.PIPE, shell=False)
git_branch = None
while True:
    line = pid_git_proc.stdout.readline()
    if not line:
        break
    print(line.rstrip(), flush=True)
    if line.rstrip().decode('utf-8').find('*') == 0:
        git_branch = line.rstrip().decode('utf-8').split(' ')[1]
        break
pid_git_proc.wait()
if git_branch is None:
    print('Can\'t find Git branch!  Exiting!')
    sys.exit()
else:
    print('Found Git branch: %s' % git_branch)

if not os.path.exists(os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment')):
    # backup to main dir with checkouts
    os.chdir(CWD_HOME_DIRECTORY)
    pid_proc = subprocess.Popen(
        shlex.split('git clone -b %s https://github.com/MediaKraken/MediaKraken_Deployment'
                    % git_branch))
    pid_proc.wait()
else:
    # cd to MediaKraken_Deployment dir
    os.chdir(os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment'))
    # pull down latest code
    pid_proc = subprocess.Popen(['git', 'pull'])
    pid_proc.wait()
    pid_proc = subprocess.Popen(['git', 'checkout', git_branch])
    pid_proc.wait()

# below is needed for the source sync to work!
os.chdir(os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment/docker/alpine'))
# sync the latest code into the image locations for build
pid_proc = subprocess.Popen(
    [os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_CI', 'source/source_sync.sh')])
pid_proc.wait()

# begin build process
if args.base:
    for build_stages in (common_docker_images.STAGE_ONE_IMAGES,
                         common_docker_images.STAGE_ONE_GAME_SERVERS,):
        build_email_push(build_stages, 'Build base dev image: ',
                         branch_tag=git_branch, push_hub_image=True)

if args.security:
    for build_stages in (common_docker_images.STAGE_ONE_SECURITY_TOOLS,
                         common_docker_images.STAGE_TWO_SECURITY_TOOLS,):
        build_email_push(build_stages, 'Build security image: ',
                         branch_tag=git_branch, push_hub_image=False)

if args.testing:
    for build_stages in (common_docker_images.STAGE_ONE_TESTING_TOOLS,
                         common_docker_images.STAGE_TWO_TESTING_TOOLS):
        build_email_push(build_stages, 'Build testing image: ',
                         branch_tag=git_branch, push_hub_image=False)

if args.version == 'dev' or args.version == 'prod':
    for build_stages in (common_docker_images.STAGE_TWO_IMAGES,
                         common_docker_images.STAGE_COMPOSE_IMAGES,
                         common_docker_images.STAGE_TWO_GAME_SERVERS):
        if args.version == 'dev':
            build_email_push(build_stages, 'Build dev image: ',
                             branch_tag=git_branch, push_hub_image=False)
        else:
            build_email_push(build_stages, 'Build prod image: ',
                             branch_tag=git_branch, push_hub_image=True)
elif args.version == 'rust':
    for file_dir in os.listdir(os.path.join(CWD_HOME_DIRECTORY,
                                            'MediaKraken_Deployment/source_rust')):
        if file_dir[0:4] == 'lib_':
            if args.image is None or (args.image is not None and file_dir == args.image):
                os.chdir(os.path.join(CWD_HOME_DIRECTORY,
                                      'MediaKraken_Deployment/source_rust', file_dir))
                pid_build_proc = subprocess.Popen(shlex.split('cargo build --release'),
                                                  stderr=subprocess.PIPE,
                                                  stdout=subprocess.PIPE)
                # print("wah", pid_build_proc.stdout, pid_build_proc.stderr)
                email_body = ''
                while True:
                    line = pid_build_proc.stderr.readline()
                    if not line:
                        break
                    email_body += line.decode("utf-8")
                    print(line.rstrip(), flush=True)
                pid_build_proc.wait()
                subject_text = ' FAILED'
                if email_body.find('Finished release') != -1:
                    subject_text = ' SUCCESS'
                    copyfile(os.path.join(CWD_HOME_DIRECTORY,
                                          'MediaKraken_Deployment/source_rust', file_dir,
                                          "target/release/libmk_%s.rlib") % file_dir,
                             os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment/source_rust',
                                          'mk_libs/libmk_%s.rlib') % file_dir)
                # send success/fail email
                common_network_email.com_net_send_email(os.environ['MAILUSER'],
                                                        os.environ['MAILPASS'],
                                                        os.environ['MAILUSER'],
                                                        file_dir
                                                        + subject_text,
                                                        email_body,
                                                        smtp_server=os.environ['MAILSERVER'],
                                                        smtp_port=os.environ['MAILPORT'])
