'''
  Copyright (C) 2019 Quinn D Granfor <spootdev@gmail.com>

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

import os
import shlex
import subprocess

from common import common_docker_images
from common import common_network_email
from dotenv import load_dotenv

# TODO proxy docker build -t mediakraken/mkbase38py3 --build-arg http_proxy="http://proxyip:8080" --build-arg ALPMIRROR=dl-cdn.alpinelinux.org --build-arg PIPMIRROR=pypi.python.org .


# load .env stats
load_dotenv()

CWD_HOME_DIRECTORY = os.getcwd().rsplit('MediaKraken_CI', 1)[0]

if not os.path.exists(os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment')):
    # backup to main dir with checkouts
    os.chdir(CWD_HOME_DIRECTORY)
    pid_proc = subprocess.Popen(
        shlex.split('git clone -b dev https://github.com/MediaKraken/MediaKraken_Deployment'))
    pid_proc.wait()
else:
    # cd to MediaKraken_Deployment dir
    os.chdir(os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment'))
    # pull down latest code
    pid_proc = subprocess.Popen(['git', 'pull'])
    pid_proc.wait()

# sync the latest code into the image locations for build
os.chdir(os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment/docker/alpine'))
pid_proc = subprocess.Popen(
    [os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_CI', 'source/source_sync.sh')])
pid_proc.wait()

for build_stages in (common_docker_images.STAGE_ONE_IMAGES,
                     common_docker_images.STAGE_TWO_IMAGES,
                     common_docker_images.STAGE_COMPOSE_IMAGES):
    for docker_images in build_stages:
        # do the actual build process for docker image
        try:
            # catch images that are in a testing branch that might not exist
            os.chdir(os.path.join(CWD_HOME_DIRECTORY,
                                  'MediaKraken_Deployment/docker',
                                  build_stages[docker_images][2], docker_images))
        except FileNotFoundError:
            continue
        # parse dockerfile for best practices
        pid_proc = subprocess.Popen(
            shlex.split('docker run --rm -i hadolint/hadolint < Dockerfile'),
            stdout=subprocess.PIPE, shell=False)
        while True:
            line = pid_proc.stdout.readline()
            if not line:
                break
            print(line.rstrip())
        pid_proc.wait()
        # TODO check for errors/warnings and stop if found
        # Successfully tagged
        # TODO don't pass alpine mirror to non alpine images?
        pid_proc = subprocess.Popen(shlex.split('docker build -t mediakraken/%s:dev'
                                                ' --build-arg ALPMIRROR=%s'
                                                ' --build-arg PIPMIRROR=%s .' %
                                                (build_stages[docker_images][0],
                                                 common_docker_images.ALPINE_MIRROR,
                                                 common_docker_images.PYPI_MIRROR)),
                                    stdout=subprocess.PIPE, shell=False)
        email_body = ''
        while True:
            line = pid_proc.stdout.readline()
            if not line:
                break
            email_body += line.decode("utf-8")
            print(line.rstrip())
        pid_proc.wait()
        subject_text = ' FAILED'
        if email_body.find('Successfully tagged mediakraken') != -1:
            subject_text = ' SUCCESS'
            # tag for local repo
            pid_proc = subprocess.Popen(
                shlex.split('docker tag mediakraken/%s:dev %s/mediakraken/%s:dev'
                            % (build_stages[docker_images][0],
                               common_docker_images.DOCKER_REPOSITORY,
                               build_stages[docker_images][0])),
                stdout=subprocess.PIPE, shell=False)
            while True:
                line = pid_proc.stdout.readline()
                if not line:
                    break
                print(line.rstrip())
            pid_proc.wait()
            # push to local repo
            pid_proc = subprocess.Popen(
                shlex.split('docker push %s/mediakraken/%s:dev'
                            % (common_docker_images.DOCKER_REPOSITORY,
                               build_stages[docker_images][0])),
                stdout=subprocess.PIPE, shell=False)
            while True:
                line = pid_proc.stdout.readline()
                if not line:
                    break
                print(line.rstrip())
            pid_proc.wait()
        # send success/fail email
        common_network_email.com_net_send_email(os.environ['MAILUSER'], os.environ['MAILPASS'],
                                                os.environ['MAILUSER'],
                                                'Build image: '
                                                + build_stages[docker_images][0]
                                                + subject_text,
                                                email_body,
                                                smtp_server=os.environ['MAILSERVER'],
                                                smtp_port=os.environ['MAILPORT'])

# # build the docker-compose images
# for build_stages in (common_docker_images.STAGE_COMPOSE_IMAGES):
#     for docker_images in build_stages:
#         # do the actual build process for docker image
#         os.chdir(os.path.join(CWD_HOME_DIRECTORY,
#                               'MediaKraken_Deployment/docker',
#                               build_stages[docker_images][2], docker_images))
