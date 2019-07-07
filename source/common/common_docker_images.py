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

ALPINE_MIRROR = 'dl-cdn.alpinelinux.org'

PYPI_MIRROR = 'pypi.python.org'

DOCKER_REPOSITORY = 'localhost:50000'  # https://index.docker.io:443

# TODO?
# ComposeMediaKrakenBasePYPY
# ComposeMediaKrakenCertBot
# ComposeMediaKrakenDMS
# ComposeMediaKrakenGameData
# ComposeMediaKrakenInotify
# ComposeMediaKrakenMythTV
# ComposeMediaKrakenPrefetchTMDB
# ComposeMediaKrakenPrefetchTVMaze
# ComposeMediaKrakenRipper

# TODO user fix for security
# Redis
# RabbitMQ
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
STAGE_ONE_IMAGES = {'ComposeMediaKrakenBase38Py3': ('mkbase38py3', 'alpine:3.8'),
                    'ComposeMediaKrakenBase39Py3': ('mkbase39py3', 'alpine:3.9'),
                    'ComposeMediaKrakenBase310Py3': ('mkbase310py3', 'alpine:3.10'),
                    'ComposeMediaKrakenBaseFFMPEG': ('mkbaseffmpeg', 'alpine:3.10'),
                    # 'ComposeMediaKrakenBaseFFMPEGUbuntu': ('mkbaseffmpegubuntu', 'ubuntu:18.10'),
                    'ComposeMediaKrakenBaseNodeJS': ('mkbasenode', 'alpine:3.9'),
                    'ComposeMediaKrakenDosBoxWeb': ('mkdosboxweb', 'ubuntu:18.04'),
                    'ComposeMediaKrakenMumble': ('mkmumble', 'alpine:3.6'),
                    'ComposeMediaKrakenMusicBrainz': ('mkmusicbrainz', 'lsiobase/alpine:3.6'),
                    'ComposeMediaKrakenRetroArchWeb': ('mkretroarchweb', 'debian:stretch'),
                    'ComposeMediaKrakenTeamspeak': ('mkteamspeak', 'alpine:3.8'),
                    'ComposeMediaKrakenTransmission': ('mktransmission', 'alpine:3.8'),
                    }

# build on top of base os images from above
STAGE_TWO_IMAGES = {'ComposeMediaKrakenBaseNodeFFMPEG': ('mkbasenodeffmpeg', 'mkbaseffmpeg'),
                    #'ComposeMediaKrakenBaseNodeFFMPEGUbuntu': (
                    #    'mkbasenodeffmpegubuntu', 'mkbaseffmpegubuntu'),
                    'ComposeMediaKrakenCastImage': ('mkcastimage', 'mkbase38py3'),
                    'ComposeMediaKrakenDevicescan': ('mkdevicescan', 'mkbase38py3'),
                    'ComposeMediaKrakenGrapesJS': ('mkgrapesjs', 'mkbasenode'),
                    'ComposeMediaKrakenSlave': ('mkslave', 'mkbasenodeffmpeg'),
                    # 'ComposeMediaKrakenSlaveUbuntu': ('mkslaveubuntu', 'mkbasenodeffmpegubuntu'),
                    'ComposeMediaKrakenTwitchRecordUser': ('mktwitchrecorduser', 'mkbase38py3')}

# these are the final "compose" images
STAGE_THREE_IMAGES = {'ComposeMediaKrakenBroadcast': ('mkbroadcast', 'mkbase38py3'),
                      'ComposeMediaKrakenCron': ('mkcron', 'mkbase310py3'),
                      'ComposeMediaKrakenDatabase': ('mkdatabase', 'alpine:3.10'),
                      'ComposeMediaKrakenDownload': ('mkdownload', 'mkbase38py3'),
                      'ComposeMediaKrakenFFProbe': ('mkffprobe', 'mkbaseffmpeg'),
                      'ComposeMediaKrakenHardware': ('mkhardware', 'mkbase38py3'),
                      'ComposeMediaKrakenMetadata': ('mkmetadata', 'mkbase38py3'),
                      'ComposeMediaKrakenNginx': ('mknginx', 'alpine:3.9'),
                      'ComposeMediaKrakenPGBouncer': ('mkpgbounce', 'alpine:3.8'),
                      'ComposeMediaKrakenPika': ('mkpika', 'mkbase310py3'),
                      'ComposeMediaKrakenRabbitMQ': ('mkrabbitmq', 'alpine:3.8'),
                      'ComposeMediaKrakenReactor': ('mkreactor', 'mkbase310py3'),
                      'ComposeMediaKrakenRedis': ('mkredis', 'alpine:3.8'),
                      'ComposeMediaKrakenRokuThumb': ('mkrokuthumb', 'mkbasenodeffmpeg'),
                      'ComposeMediaKrakenServer': ('mkserver', 'mkbase38py3'),
                      'ComposeMediaKrakenWebServer': ('mkwebapp', 'mkbase38py3'),
                      }

# these are for security and linting all code
# directory, name, base image, build script
STAGE_ONE_SECURITY_TOOLS = {'elk': ('mkelk', 'phusion/baseimage:0.11'),
                            'jenkins': ('mkjenkins', 'jenkins/jenkins:lts'),
                            'kali': ('mkkali', 'kalilinux/kali-linux-docker', './build.sh'),
                            'pgadmin4': ('mkpgadmin', 'python:alpine3.9'),
                            'testssl': ('mktestssl', 'alpine:3.9'),
                            'wireshark': ('mkwireshark', 'debian:stretch-slim'),
                            }

STAGE_TWO_SECURITY_TOOLS = {
    'rapidscan': ('mkrapidscan', 'mkkali'),
}
