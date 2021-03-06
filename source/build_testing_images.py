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

# load .env stats
load_dotenv()

CWD_HOME_DIRECTORY = os.getcwd().rsplit('MediaKraken_CI', 1)[0]
for build_stages in (common_docker_images.STAGE_ONE_TESTING_TOOLS,
                     common_docker_images.STAGE_TWO_TESTING_TOOLS):
    for docker_images in build_stages:
        os.chdir(os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_CI', 'docker/%s' % docker_images))
        print(os.getcwd(), flush=True)
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
            print(line.rstrip(), flush=True)
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
                print(line.rstrip(), flush=True)
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
                print(line.rstrip(), flush=True)
            pid_proc.wait()
        # send success/fail email
        common_network_email.com_net_send_email(os.environ['MAILUSER'], os.environ['MAILPASS'],
                                                os.environ['MAILUSER'],
                                                'Build testing image: '
                                                + build_stages[docker_images][0]
                                                + subject_text,
                                                email_body,
                                                smtp_server=os.environ['MAILSERVER'],
                                                smtp_port=os.environ['MAILPORT'])
