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
import shutil
import subprocess

from common import common_docker_images

# change this directory to the dir that you have MediaKraken_CI checked out too
CWD_HOME_DIRECTORY = '/root'

if not os.path.exists(os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment')):
    # backup to main dir with checkouts
    os.chdir(CWD_HOME_DIRECTORY)
    pid_proc = subprocess.Popen(
        shlex.split('git clone -b dev https://github.com/MediaKraken/MediaKraken_Deployment'))
    pid_proc.wait()
    os.chdir(os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment/docker/alpine'))
else:
    # cd to MediaKraken_Deployment dir
    os.chdir(os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_Deployment/docker/alpine'))
    # pull down latest code
    pid_proc = subprocess.Popen(['git', 'pull'])
    pid_proc.wait()

# sync the latest code into the image locations for build
pid_proc = subprocess.Popen(
    [os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_CI', 'source/source_sync.sh')])
pid_proc.wait()

for build_stages in (common_docker_images.STAGE_ONE_IMAGES,
                     common_docker_images.STAGE_TWO_IMAGES,
                     common_docker_images.STAGE_THREE_IMAGES):
    for docker_images in build_stages:
        # do the actual build process for docker image
        os.chdir(os.path.join(CWD_HOME_DIRECTORY,
                              'MediaKraken_Deployment/docker/alpine/%s' % docker_images))
        pid_proc = subprocess.Popen(shlex.split('docker build -t mediakraken/%s:dev'
                                                ' --build-arg ALPMIRROR=%s'
                                                ' --build-arg PIPMIRROR=%s .') %
                                    (build_stages[docker_images][0],
                                     common_docker_images.ALPINE_MIRROR,
                                     common_docker_images.PYPI_MIRROR))
        pid_proc.wait()
