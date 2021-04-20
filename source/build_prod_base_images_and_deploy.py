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

# must login to docker hub first
# docker login --username=mediakraken

import shlex
import subprocess

from common import common_docker_images

for build_stages in (common_docker_images.STAGE_ONE_IMAGES,
                     common_docker_images.STAGE_TWO_IMAGES,
                     common_docker_images.STAGE_ONE_GAME_SERVERS,
                     ):
    for docker_images in build_stages:
        # retag all the images to latest
        pid_proc = subprocess.Popen(
            shlex.split('docker tag mediakraken/%s:dev mediakraken/%s:latest'
                        % (build_stages[docker_images][0], build_stages[docker_images][0])),
            stdout=subprocess.PIPE, shell=False)
        while True:
            line = pid_proc.stdout.readline()
            if not line:
                break
            print(line.rstrip(), flush=True)
        pid_proc.wait()
        # push the actual image to docker hub
        pid_proc = subprocess.Popen(
            shlex.split('docker push mediakraken/%s:latest' % build_stages[docker_images][0]),
            stdout=subprocess.PIPE, shell=False)
        while True:
            line = pid_proc.stdout.readline()
            if not line:
                break
            print(line.rstrip(), flush=True)
        pid_proc.wait()
