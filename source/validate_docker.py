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

import os
import shlex
import subprocess
import sys

from dotenv import load_dotenv

from common import common_docker_images
from common import common_network_email

# load .env stats
load_dotenv()

CWD_HOME_DIRECTORY = os.getcwd().rsplit('MediaKraken_CI', 1)[0]
print(CWD_HOME_DIRECTORY, flush=True)

# hadolint - lint your Dockerfile
# don't do the testing/security images as they aren't MK production code
for build_stages in (common_docker_images.STAGE_ONE_IMAGES,
                     common_docker_images.STAGE_TWO_IMAGES,
                     common_docker_images.STAGE_COMPOSE_IMAGES,
                     common_docker_images.STAGE_ONE_FS,
                     common_docker_images.STAGE_ONE_GAME_SERVERS,
                     common_docker_images.STAGE_TWO_GAME_SERVERS):
    for docker_images in build_stages:
        print('hado docker:', docker_images)
        os.chdir(os.path.join(CWD_HOME_DIRECTORY,
                              'MediaKraken_Deployment/docker',
                              build_stages[docker_images][2], docker_images))
        # Run hadolint on each image
        try:
            pid_proc = subprocess.Popen(
                shlex.split('hadolint Dockerfile'),
                stdout=subprocess.PIPE, shell=False)
        except subprocess.CalledProcessError as e:
            print(e.output, flush=True)
            sys.exit()
        email_body = ''
        try:
            while True:
                line = pid_proc.stdout.readline()
                if not line:
                    break
                email_body += line.decode("utf-8")
                print(line.rstrip(), flush=True)
            pid_proc.wait()
        except:
            pass
        if email_body == '':
            error_status = ' SUCCESS'
        else:
            error_status = ' FAILED'
        common_network_email.com_net_send_email(os.environ['MAILUSER'], os.environ['MAILPASS'],
                                                os.environ['MAILUSER'],
                                                'Hadolint image: '
                                                + build_stages[docker_images][0]
                                                + error_status,
                                                email_body,
                                                smtp_server=os.environ['MAILSERVER'],
                                                smtp_port=os.environ['MAILPORT'])

# trivy - security scan docker images
# don't do the testing/security images as they aren't MK production code
for build_stages in (common_docker_images.STAGE_ONE_IMAGES,
                     common_docker_images.STAGE_TWO_IMAGES,
                     common_docker_images.STAGE_COMPOSE_IMAGES,
                     common_docker_images.STAGE_ONE_FS,
                     common_docker_images.STAGE_ONE_GAME_SERVERS,
                     common_docker_images.STAGE_TWO_GAME_SERVERS):
    for docker_images in build_stages:
        # Run trivy on each image
        try:
            pid_proc = subprocess.Popen(
                shlex.split('trivy image %s/mediakraken/%s:dev' %
                            (common_docker_images.DOCKER_REPOSITORY,
                             build_stages[docker_images][0])),
                stdout=subprocess.PIPE, shell=False)
        except subprocess.CalledProcessError as e:
            print(e.output, flush=True)
            sys.exit()
        email_body = ''
        error_status = ' FAILED'
        try:
            while True:
                line = pid_proc.stdout.readline()
                if not line:
                    break
                email_body += line.decode("utf-8")
                print(line.rstrip(), flush=True)
                if line.find('Total: 0 (') != -1:
                    error_status = ' SUCCESS'
            pid_proc.wait()
        except:
            pass
        common_network_email.com_net_send_email(os.environ['MAILUSER'], os.environ['MAILPASS'],
                                                os.environ['MAILUSER'],
                                                'Trivy image: '
                                                + build_stages[docker_images][0]
                                                + error_status,
                                                email_body,
                                                smtp_server=os.environ['MAILSERVER'],
                                                smtp_port=os.environ['MAILPORT'])
