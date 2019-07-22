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

ALPINE_MIRROR = '10.0.0.122'

PYPI_MIRROR = 'th-bandersnatch-1' # pypi.python.org

DOCKER_REPOSITORY = 'th-registry-1.beaverbay.local'  # https://index.docker.io:443

# TODO?
# ComposeMediaKrakenBasePYPY
# ComposeMediaKrakenCertBot
# ComposeMediaKrakenDMS
# ComposeMediaKrakenGameData
# ComposeMediaKrakenInotify
# ComposeMediaKrakenMythTV
# ComposeMediaKrakenPrefetchTMDB
# ComposeMediaKrakenPrefetchTVMaze

# TODO user fix for security
# Redis
# RabbitMQ
# Ripper
# NGINX
# Database
# Transmission
# Teamspeak
# RetroArchWeb
# MusicBrainz

'''
FROM node:10-alpine 
RUN mkdir /app
COPY . /app
RUN chown -R node:node /app
USER node
CMD [“node”, “index.js”]
'''

# the data is directory, name of container, base image used to build container

# base OS images to build off of, meaning there is a 'from' in the docker file(s) that use these
STAGE_ONE_IMAGES = {'ComposeMediaKrakenBase38Py3': ('mkbase38py3', 'alpine:3.8', 'alpine'),
                    'ComposeMediaKrakenBase39Py3': ('mkbase39py3', 'alpine:3.9', 'alpine'),
                    'ComposeMediaKrakenBase310Py3': ('mkbase310py3', 'alpine:3.10', 'alpine'),
                    'ComposeMediaKrakenBaseFFMPEG': ('mkbaseffmpeg', 'alpine:3.10', 'alpine'),
                    # 'ComposeMediaKrakenBaseFFMPEGUbuntu': ('mkbaseffmpegubuntu', 'ubuntu:18.10', 'ubuntu'),
                    'ComposeMediaKrakenBaseNodeJS': ('mkbasenode', 'alpine:3.9', 'alpine'),
                    'ComposeMediaKrakenDosBoxWeb': ('mkdosboxweb', 'ubuntu:18.04', 'ubuntu'),
                    'ComposeMediaKrakenMumble': ('mkmumble', 'alpine:3.6', 'alpine'),
                    'ComposeMediaKrakenMusicBrainz': ('mkmusicbrainz', 'lsiobase/alpine:3.6', 'alpine'),
                    'ComposeMediaKrakenRetroArchWeb': ('mkretroarchweb', 'debian:stretch', 'debian'),
                    'ComposeMediaKrakenTeamspeak': ('mkteamspeak', 'alpine:3.8', 'alpine'),
                    'ComposeMediaKrakenTransmission': ('mktransmission', 'alpine:3.8', 'alpine'),
                    }

# build on top of base os images from above
STAGE_TWO_IMAGES = {'ComposeMediaKrakenBaseNodeFFMPEG': ('mkbasenodeffmpeg', 'mkbaseffmpeg', 'alpine'),
                    #'ComposeMediaKrakenBaseNodeFFMPEGUbuntu': (
                    #    'mkbasenodeffmpegubuntu', 'mkbaseffmpegubuntu', 'ubuntu'),
                    'ComposeMediaKrakenCastImage': ('mkcastimage', 'mkbase38py3', 'alpine'),
                    'ComposeMediaKrakenDevicescan': ('mkdevicescan', 'mkbase38py3', 'alpine'),
                    'ComposeMediaKrakenGrapesJS': ('mkgrapesjs', 'mkbasenode', 'alpine'),
                    'ComposeMediaKrakenRipper': ('mkripper', 'mkbaseffmpeg', 'alpine'),
                    'ComposeMediaKrakenSlave': ('mkslave', 'mkbasenodeffmpeg', 'alpine'),
                    # 'ComposeMediaKrakenSlaveUbuntu': ('mkslaveubuntu', 'mkbasenodeffmpegubuntu', 'ubuntu'),
                    'ComposeMediaKrakenTwitchRecordUser': ('mktwitchrecorduser', 'mkbase38py3', 'alpine')}

# these are the final "compose" images
STAGE_THREE_IMAGES = {'ComposeMediaKrakenBroadcast': ('mkbroadcast', 'mkbase38py3', 'alpine'),
                      'ComposeMediaKrakenCron': ('mkcron', 'mkbase310py3', 'alpine'),
#                      'ComposeMediaKrakenDatabase': ('mkdatabase', 'alpine:3.10', 'alpine'),
                      'ComposeMediaKrakenDatabase': ('mkdatabase', 'debian:stretch-slim', 'debian'),
                      'ComposeMediaKrakenDownload': ('mkdownload', 'mkbase38py3', 'alpine'),
                      'ComposeMediaKrakenFFProbe': ('mkffprobe', 'mkbaseffmpeg', 'alpine'),
                      'ComposeMediaKrakenHardware': ('mkhardware', 'mkbase38py3', 'alpine'),
                      'ComposeMediaKrakenMetadata': ('mkmetadata', 'mkbase38py3', 'alpine'),
                      'ComposeMediaKrakenNginx': ('mknginx', 'alpine:3.9', 'alpine'),
                      'ComposeMediaKrakenPGBouncer': ('mkpgbounce', 'alpine:3.8', 'alpine'),
                      'ComposeMediaKrakenPika': ('mkpika', 'mkbase310py3', 'alpine'),
                      'ComposeMediaKrakenRabbitMQ': ('mkrabbitmq', 'alpine:3.8', 'alpine'),
                      'ComposeMediaKrakenReactor': ('mkreactor', 'mkbase310py3', 'alpine'),
                      'ComposeMediaKrakenRedis': ('mkredis', 'alpine:3.8', 'alpine'),
                      'ComposeMediaKrakenRokuThumb': ('mkrokuthumb', 'mkbasenodeffmpeg', 'alpine'),
                      'ComposeMediaKrakenServer': ('mkserver', 'mkbase38py3', 'alpine'),
                      'ComposeMediaKrakenWebServer': ('mkwebapp', 'mkbase38py3', 'alpine'),
                      }

# these are for security and linting all code
# directory, name, base image, build script
STAGE_ONE_SECURITY_TOOLS = {'elk': ('mkelk', 'phusion/baseimage:0.11'),
                            'jenkins': ('mkjenkins', 'jenkins/jenkins:lts'),
                            'kali': ('mkkali', 'kalilinux/kali-linux-docker', './build.sh'),
                            'pgadmin4': ('mkpgadmin', 'python:alpine3.9'),
                            'registry': ('mkregistry', 'alpine:3.8'),
                            'testssl': ('mktestssl', 'alpine:3.9'),
                            'wireshark': ('mkwireshark', 'debian:stretch-slim'),
                            }

STAGE_TWO_SECURITY_TOOLS = {
    'rapidscan': ('mkrapidscan', 'mkkali'),
}
