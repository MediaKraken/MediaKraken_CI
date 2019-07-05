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

CWD_HOME_DIRECTORY = os.getcwd().rsplit('\\MediaKraken_CI', 1)[0]
for build_stages in (common_docker_images.STAGE_ONE_SECURITY_TOOLS,
                     common_docker_images.STAGE_TWO_SECURITY_TOOLS,):
    for docker_images in build_stages:
        os.chdir(os.path.join(CWD_HOME_DIRECTORY, 'MediaKraken_CI', 'docker/%s' % docker_images))
        print(os.getcwd())
        pid_proc = subprocess.Popen(shlex.split('docker build -t mediakraken/%s:dev'
                                                ' --build-arg ALPMIRROR=%s'
                                                ' --build-arg PIPMIRROR=%s .' %
                                                (build_stages[docker_images][0],
                                                 common_docker_images.ALPINE_MIRROR,
                                                 common_docker_images.PYPI_MIRROR)),
                                    stdout=subprocess.PIPE, shell=False)
        while True:
            line = pid_proc.stdout.readline()
            if not line:
                break
            print(line.rstrip())
        pid_proc.wait()
