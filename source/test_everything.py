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
import sys
import time

from common import common_docker_images
from common import common_network_email
from dotenv import load_dotenv

# load .env stats
load_dotenv()

CWD_HOME_DIRECTORY = os.getcwd().rsplit('MediaKraken_CI', 1)[0]

#####################################
# lint and validate code
#####################################

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
            sys.exit()
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

# change dir for anchore scanner
os.chdir(os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_CI', 'docker/anchore/'))
for build_stages in (common_docker_images.STAGE_ONE_IMAGES,
                     common_docker_images.STAGE_TWO_IMAGES,
                     common_docker_images.STAGE_COMPOSE_IMAGES):
    for docker_images in build_stages:
        # Run Clair on each image
        try:
            pid_proc = subprocess.Popen(
                shlex.split('docker-compose exec engine-api anchore-cli image vuln'
                            ' %s/mediakraken/%s:dev all' %
                            (common_docker_images.DOCKER_REPOSITORY,
                             build_stages[docker_images][0])),
                stdout=subprocess.PIPE, shell=False)
        except subprocess.CalledProcessError as e:
            print(e.output)
            sys.exit()
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
                                                'Anchore image scan: '
                                                + build_stages[docker_images][0],
                                                email_body,
                                                smtp_server=os.environ['MAILSERVER'],
                                                smtp_port=os.environ['MAILPORT'])

# run vulture to find dead code
try:
    pid_proc = subprocess.Popen(
        shlex.split('vulture', os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment')),
        stdout=subprocess.PIPE, shell=False)
except subprocess.CalledProcessError as e:
    print(e.output)
    sys.exit()
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
                                        'Vulture (dead code)',
                                        email_body,
                                        smtp_server=os.environ['MAILSERVER'],
                                        smtp_port=os.environ['MAILPORT'])

# run Graudit to find unsecure code
try:
    pid_proc = subprocess.Popen(
        shlex.split('graudit -d python',
                    os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment')),
        stdout=subprocess.PIPE, shell=False)
except subprocess.CalledProcessError as e:
    print(e.output)
    sys.exit()
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
                                        'Graudit (Unsecure Code)',
                                        email_body,
                                        smtp_server=os.environ['MAILSERVER'],
                                        smtp_port=os.environ['MAILPORT'])

# run python taint to find unsecure code
try:
    pid_proc = subprocess.Popen(
        shlex.split('python3 -m pyt -r',
                    os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment')),
        stdout=subprocess.PIPE, shell=False)
except subprocess.CalledProcessError as e:
    print(e.output)
    sys.exit()
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
                                        'Python Taint (Unsecure Code Injection)',
                                        email_body,
                                        smtp_server=os.environ['MAILSERVER'],
                                        smtp_port=os.environ['MAILPORT'])

# run Bandit to find unsecure code
try:
    pid_proc = subprocess.Popen(
        shlex.split('bandit -r', os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment')),
        stdout=subprocess.PIPE, shell=False)
except subprocess.CalledProcessError as e:
    print(e.output)
    sys.exit()
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
                                        'Bandit (Unsecure Code)',
                                        email_body,
                                        smtp_server=os.environ['MAILSERVER'],
                                        smtp_port=os.environ['MAILPORT'])

# run radon to determine code complexity
try:
    pid_proc = subprocess.Popen(
        shlex.split('radon cc', os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment')),
        stdout=subprocess.PIPE, shell=False)
except subprocess.CalledProcessError as e:
    print(e.output)
    sys.exit()
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
                                        'Radon (Code Complexity)',
                                        email_body,
                                        smtp_server=os.environ['MAILSERVER'],
                                        smtp_port=os.environ['MAILPORT'])

# run pytype to run type checking
try:
    pid_proc = subprocess.Popen(
        shlex.split('pytype', os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment')),
        stdout=subprocess.PIPE, shell=False)
except subprocess.CalledProcessError as e:
    print(e.output)
    sys.exit()
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
                                        'Pytype (Type Checking)',
                                        email_body,
                                        smtp_server=os.environ['MAILSERVER'],
                                        smtp_port=os.environ['MAILPORT'])

# run pylama to code quality
try:
    pid_proc = subprocess.Popen(
        shlex.split('pylama', os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment')),
        stdout=subprocess.PIPE, shell=False)
except subprocess.CalledProcessError as e:
    print(e.output)
    sys.exit()
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
                                        'Pylama (Code Quality)',
                                        email_body,
                                        smtp_server=os.environ['MAILSERVER'],
                                        smtp_port=os.environ['MAILPORT'])

#####################################
# start up the application so can see running images for several tools
#####################################
os.chdir(os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment', 'docker/swarm/'))
pid_proc = subprocess.Popen(shlex.split('mediakraken_start.sh'),
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

# run under started app as need the db connection
# TODO that won't work.....as it's a docker db
pytest_pid = subprocess.Popen(shlex.split(
    'python3 -m pytest --capture=no testing/test_common/test_common_network_youtube.py'))
pytest_pid.wait()

#####################################
# run application web test/etc
#####################################

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

# run nikto web scanner
pid_proc = subprocess.Popen(shlex.split('docker run -ti %s/mediakraken/mknikto:dev -h '
                                        'localhost:8900'
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
                                        'Nitko', email_body,
                                        smtp_server=os.environ['MAILSERVER'],
                                        smtp_port=os.environ['MAILPORT'])

# run sitadel web security scanner
pid_proc = subprocess.Popen(shlex.split('docker run -ti %s/mediakraken/mksitadel:dev -h '
                                        'localhost:8900'
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
                                        'sitadel', email_body,
                                        smtp_server=os.environ['MAILSERVER'],
                                        smtp_port=os.environ['MAILPORT'])

#####################################
# stop the application
#####################################
os.chdir(os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment', 'docker/swarm/'))
pid_proc = subprocess.Popen(shlex.split('mediakraken_stop.sh'),
                            stdout=subprocess.PIPE, shell=False)
