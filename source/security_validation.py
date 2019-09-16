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
import time

from common import common_docker_images
from common import common_network_email
from dotenv import load_dotenv

# load .env stats
load_dotenv()

CWD_HOME_DIRECTORY = os.getcwd().rsplit('MediaKraken_CI', 1)[0]

# change dir for clair scanner
os.chdir(os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_CI', 'docker/clair/'))
for build_stages in (common_docker_images.STAGE_ONE_IMAGES,
                     common_docker_images.STAGE_TWO_IMAGES,
                     common_docker_images.STAGE_COMPOSE_IMAGES):
    for docker_images in build_stages:
        # Run Clair on each image
        try:
            pid_proc = subprocess.Popen(
                shlex.split('docker-compose run --rm clair-scanner %s/mediakraken/%s:dev' %
                            (common_docker_images.DOCKER_REPOSITORY,
                             build_stages[docker_images][0])),
                stdout=subprocess.PIPE, shell=False)
        except subprocess.CalledProcessError as e:
            print(e.output)
        email_body = ''
        try:
            while True:
                line = pid_proc.stdout.readline()
                if not line:
                    break
                email_body += line.decode("utf-8")
                print(line.rstrip())
            pid_proc.wait()
        except:
            pass
        common_network_email.com_net_send_email(os.environ['MAILUSER'], os.environ['MAILPASS'],
                                                os.environ['MAILUSER'],
                                                'Clair image: '
                                                + build_stages[docker_images][0],
                                                email_body,
                                                smtp_server=os.environ['MAILSERVER'],
                                                smtp_port=os.environ['MAILPORT'])

# Start up the app so bench can see running images
os.chdir(os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment', 'docker/swarm/'))
pid_proc = subprocess.Popen(shlex.split('./mediakraken_start.sh'),
                            stdout=subprocess.PIPE, shell=False)
while True:
    line = pid_proc.stdout.readline()
    if not line:
        break
    print(line.rstrip())
pid_proc.wait()
# this sleep is here so that everything has time to fully start like pika
time.sleep(60)

# run docker-bench on all images as it checks for common best practices
os.chdir(os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_CI', 'source'))
pid_proc = subprocess.Popen(shlex.split('./bench.sh'),
                            stdout=subprocess.PIPE, shell=False)
email_body = ''
while True:
    line = pid_proc.stdout.readline()
    if not line:
        break
    email_body += line.decode("utf-8")
    print(line.rstrip())
pid_proc.wait()
common_network_email.com_net_send_email(os.environ['MAILUSER'], os.environ['MAILPASS'],
                                        os.environ['MAILUSER'],
                                        'Docker Bench', email_body,
                                        smtp_server=os.environ['MAILSERVER'],
                                        smtp_port=os.environ['MAILPORT'])

# Test the SSL security of the nginx ssl setup via testssl.sh
pid_proc = subprocess.Popen(shlex.split('docker run -ti %s/mediakraken/mktestssl:dev localhost:8900'
                                        % (common_docker_images.DOCKER_REPOSITORY,)),
                            stdout=subprocess.PIPE, shell=False)
email_body = ''
while True:
    line = pid_proc.stdout.readline()
    if not line:
        break
    email_body += line.decode("utf-8")
    print(line.rstrip())
pid_proc.wait()
common_network_email.com_net_send_email(os.environ['MAILUSER'], os.environ['MAILPASS'],
                                        os.environ['MAILUSER'],
                                        'TestSSL', email_body,
                                        smtp_server=os.environ['MAILSERVER'],
                                        smtp_port=os.environ['MAILPORT'])

# Web Vulnerability Scanner via rapidscan
pid_proc = subprocess.Popen(
    shlex.split(
        'docker run -ti %s/mediakraken/mkrapidscan:dev localhost:8900' %
        (common_docker_images.DOCKER_REPOSITORY,)),
    stdout=subprocess.PIPE, shell=False)
email_body = ''
while True:
    line = pid_proc.stdout.readline()
    if not line:
        break
    email_body += line.decode("utf-8")
    print(line.rstrip())
pid_proc.wait()
common_network_email.com_net_send_email(os.environ['MAILUSER'], os.environ['MAILPASS'],
                                        os.environ['MAILUSER'],
                                        'Rapidscan', email_body,
                                        smtp_server=os.environ['MAILSERVER'],
                                        smtp_port=os.environ['MAILPORT'])

# stop the services
os.chdir(os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment', 'docker/swarm/'))
pid_proc = subprocess.Popen(shlex.split('./mediakraken_stop.sh'),
                            stdout=subprocess.PIPE, shell=False)
