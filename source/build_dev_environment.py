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

centos_packages = {'python3-devel'}
debian_packages = {}
# install base packages per OS (centos, debian)
pid_proc = subprocess.Popen(shlex.split('yum install -y', centos_packages),
                            stdout=subprocess.PIPE, shell=False)
pid_proc.wait()

# install pypi packages
pid_proc = subprocess.Popen(shlex.split('pip3 install -r requirements.txt'),
                            stdout=subprocess.PIPE, shell=False)
pid_proc.wait()

# Dockerfile linter
pid_proc = subprocess.Popen(shlex.split('docker pull hadolint/hadolint'),
                            stdout=subprocess.PIPE, shell=False)
pid_proc.wait()

# Download all the images for Clair
os.chdir('../docker/clair')
pid_proc = subprocess.Popen(shlex.split('docker-compose pull'),
                            stdout=subprocess.PIPE, shell=False)
pid_proc.wait()

# Download all the images for Mailcow
os.chdir('../docker/mailcow')
pid_proc = subprocess.Popen(shlex.split('docker-compose pull'),
                            stdout=subprocess.PIPE, shell=False)
pid_proc.wait()
