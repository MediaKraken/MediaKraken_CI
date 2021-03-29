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

from common import common_network_email

# load .env stats
load_dotenv()

CWD_HOME_DIRECTORY = os.getcwd().rsplit('MediaKraken_CI', 1)[0]
print(CWD_HOME_DIRECTORY, flush=True)

# run Bandit to find unsecured code
try:
    print('Bandit & %s' % os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment'), flush=True)
    pid_proc = subprocess.Popen(
        shlex.split('bandit -r %s' % os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment')),
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
common_network_email.com_net_send_email(os.environ['MAILUSER'], os.environ['MAILPASS'],
                                        os.environ['MAILUSER'],
                                        'Bandit (Unsecure Code)',
                                        email_body,
                                        smtp_server=os.environ['MAILSERVER'],
                                        smtp_port=os.environ['MAILPORT'])

# run vulture to find dead code
try:
    print('Vulture & %s' % os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment'), flush=True)
    pid_proc = subprocess.Popen(
        shlex.split('vulture %s' % os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment')),
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
common_network_email.com_net_send_email(os.environ['MAILUSER'], os.environ['MAILPASS'],
                                        os.environ['MAILUSER'],
                                        'Vulture (dead code)',
                                        email_body,
                                        smtp_server=os.environ['MAILSERVER'],
                                        smtp_port=os.environ['MAILPORT'])

# run python taint to find unsecured code
try:
    print('Taint & %s' % os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment'), flush=True)
    pid_proc = subprocess.Popen(
        shlex.split('python3 -m pyt -r %s' %
                    os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment')),
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
common_network_email.com_net_send_email(os.environ['MAILUSER'], os.environ['MAILPASS'],
                                        os.environ['MAILUSER'],
                                        'Python Taint (Unsecure Code Injection)',
                                        email_body,
                                        smtp_server=os.environ['MAILSERVER'],
                                        smtp_port=os.environ['MAILPORT'])
