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

"""
MUST RUN FROM THE SOURCE DIRECTORY IN THE CI PROJECT
MUST RUN FROM THE SOURCE DIRECTORY IN THE CI PROJECT
MUST RUN FROM THE SOURCE DIRECTORY IN THE CI PROJECT
MUST RUN FROM THE SOURCE DIRECTORY IN THE CI PROJECT
MUST RUN FROM THE SOURCE DIRECTORY IN THE CI PROJECT
MUST RUN FROM THE SOURCE DIRECTORY IN THE CI PROJECT
MUST RUN FROM THE SOURCE DIRECTORY IN THE CI PROJECT
"""

if not os.path.exists('../../MediaKraken_Deployment'):
    # backup to main dir with checkouts
    subprocess.Popen(shlex.split('cd ../../'))
    subprocess.Popen(
        shlex.split('git clone -b dev https://github.com/MediaKraken/MediaKraken_Deployment'))
    subprocess.Popen(shlex.split('cd ./MediaKraken_Deployment/docker/alpine'))
else:
    # cd to MediaKraken_Deployment dir
    subprocess.Popen(shlex.split('cd ../../MediaKraken_Deployment//docker/alpine'))
    # pull down latest code
    subprocess.Popen(['git', 'pull'])

# sync the latest code into the image locations for build
# broadcast
shutil.copy('../../source/subprogram_broadcast.py', './ComposeMediaKrakenBroadcast/src/')
shutil.copytree('../../source/common', './ComposeMediaKrakenBroadcast/src/')

# os.subprocess.Popen(['./source_sync.sh'])

for build_stages in (common_docker_images.STAGE_ONE_IMAGES,
                     common_docker_images.STAGE_TWO_IMAGES,
                     common_docker_images.STAGE_THREE_IMAGES):
    for docker_images in build_stages:
        # do the actual build process for docker image
        subprocess.Popen(shlex.split('cd ../%s && docker build -t mediakraken/%s:dev'
                                     ' --build-arg ALPMIRROR=%s --build-arg PIPMIRROR=%s .') %
                         (docker_images, build_stages[docker_images][0],
                          common_docker_images.ALPINE_MIRROR,
                          common_docker_images.PYPI_MIRROR))
