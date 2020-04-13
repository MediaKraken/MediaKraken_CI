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

# ALPINE_MIRROR = 'th-alpinemirror-1.beaverbay.local'
ALPINE_MIRROR = 'dl-2.alpinelinux.org'

# PYPI_MIRROR = 'th-bandersnatch-1'  # pypi.python.org
PYPI_MIRROR = 'pypi.python.org'

DOCKER_REPOSITORY = 'th-registry-1.beaverbay.local:5000'  # https://index.docker.io:443

PROXY_IP_PORT = '0.0.0.0:8080'
PROXY_USER_NAME = None
PROXY_USER_PASS = None

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
CMD ["node", "index.js"]
'''

# the data is directory, name of container, base image used to build container

# base OS images to build off of, meaning there is a 'from' in the docker file(s) that use these
STAGE_ONE_IMAGES = {'ComposeMediaKrakenBase38Py3': ('mkbase38py3', 'alpine:3.8', 'alpine'),
                    'ComposeMediaKrakenBase39Py3': ('mkbase39py3', 'alpine:3.9', 'alpine'),
                    'ComposeMediaKrakenBase310Py3': ('mkbase310py3', 'alpine:3.10', 'alpine'),
                    'ComposeMediaKrakenBase310_1Py3': ('mkbase310_1py3', 'alpine:3.10.1', 'alpine'),
                    'ComposeMediaKrakenBase310_2Py3': ('mkbase310_2py3', 'alpine:3.10.2', 'alpine'),
                    'ComposeMediaKrakenBase311_3Py3': ('mkbase311_3py3', 'alpine:3.11.3', 'alpine'),
                    'ComposeMediaKrakenBase311_5Py3': ('mkbase311_5py3', 'alpine:3.11.5', 'alpine'),
                    'ComposeMediaKrakenBase9_9Py3': ('mkbasedeb9_9py3', 'debian:9.9-slim', 'debian'),
                    'ComposeMediaKrakenBase10_2Py3': ('mkbasedeb10_2py3', 'debian:10.2-slim', 'debian'),
                    'ComposeMediaKrakenBase10_3Py3': ('mkbasedeb10_3py3', 'debian:10.3-slim', 'debian'),
                    'ComposeMediaKrakenBaseFFMPEG': ('mkbaseffmpeg', 'alpine:3.11.3', 'alpine'),
                    'ComposeMediaKrakenBaseNodeJS': ('mkbasenode', 'alpine:3.9', 'alpine'),
                    'ComposeMediaKrakenBaseSteamCMD': ('mkbasesteamcmd', 'debian:10.3-slim', 'debian'),
                    'ComposeMediaKrakenDosBoxWeb': ('mkdosboxweb', 'ubuntu:18.04', 'ubuntu'),
                    'ComposeMediaKrakenMumble': ('mkmumble', 'alpine:3.6', 'alpine'),
                    'ComposeMediaKrakenMusicBrainz': ('mkmusicbrainz', 'lsiobase/alpine:3.6', 'alpine'),
                    'ComposeMediaKrakenRetroArchWeb': ('mkretroarchweb', 'debian:stretch', 'debian'),
                    'ComposeMediaKrakenTeamspeak': ('mkteamspeak', 'alpine:3.8', 'alpine'),
                    'ComposeMediaKrakenTransmission': ('mktransmission', 'alpine:3.8', 'alpine'),
                    }

# build on top of base os images from above
STAGE_TWO_IMAGES = {
    'ComposeMediaKrakenBaseNodeFFMPEG': ('mkbasenodeffmpeg', 'mkbaseffmpeg', 'alpine'),
    'ComposeMediaKrakenCastImage': ('mkcastimage', 'mkbase311_5py3', 'alpine'),
    'ComposeMediaKrakenDevicescan': ('mkdevicescan', 'mkbase311_5py3', 'alpine'),
    'ComposeMediaKrakenRipper': ('mkripper', 'mkbaseffmpeg', 'alpine'),
    'ComposeMediaKrakenSlave': ('mkslave', 'mkbasenodeffmpeg', 'alpine'),
    'ComposeMediaKrakenTwitchRecordUser': ('mktwitchrecorduser', 'mkbase311_5py3', 'alpine')}

# these are the final "compose" images
STAGE_COMPOSE_IMAGES = {'ComposeMediaKrakenBarman': ('mkbarman', 'debian:jessie', 'debian'),
                        'ComposeMediaKrakenBroadcast': ('mkbroadcast', 'mkbase311_5py3', 'alpine'),
                        'ComposeMediaKrakenConsul': ('mkconsul', 'alpine:3.9', 'alpine'),
                        'ComposeMediaKrakenCron': ('mkcron', 'mkbase311_5py3', 'alpine'),
                        'ComposeMediaKrakenDatabase11_7': (
                            'mkdatabase', 'debian:9.9-slim', 'debian'),
                        'ComposeMediaKrakenDownload': ('mkdownload', 'mkbase311_5py3', 'alpine'),
                        'ComposeMediaKrakenFFProbe': ('mkffprobe', 'mkbaseffmpeg', 'alpine'),
                        'ComposeMediaKrakenHAProxy': ('mkpghaproxy', 'alpine:3.10', 'alpine'),
                        'ComposeMediaKrakenHardware': ('mkhardware', 'mkbase311_5py3', 'alpine'),
                        'ComposeMediaKrakenLDAP': ('mkldap', 'lsiobase/alpine:3.11', 'alpine'),
                        'ComposeMediaKrakenMetadata': ('mkmetadata', 'mkbase311_5py3', 'alpine'),
                        'ComposeMediaKrakenNginx': ('mknginx', 'alpine:3.10', 'alpine'),
                        'ComposeMediaKrakenNginxPagespeed': ('mknginxpagespeed', 'alpine:3.8', 'alpine'),
                        'ComposeMediaKrakenOdyssey': ('mkodyssey', 'debian:9.9-slim', 'debian'),
                        'ComposeMediaKrakenPGBouncer': ('mkpgbouncer', 'alpine:3.11.5', 'alpine'),
                        'ComposeMediaKrakenPika': ('mkpika', 'mkbase311_5py3', 'alpine'),
                        'ComposeMediaKrakenRabbitMQ': ('mkrabbitmq', 'alpine:3.11', 'alpine'),
                        'ComposeMediaKrakenReactor': ('mkreactor', 'mkbase311_5py3', 'alpine'),
                        'ComposeMediaKrakenRokuThumb': (
                            'mkrokuthumb', 'mkbasenodeffmpeg', 'alpine'),
                        'ComposeMediaKrakenServer': ('mkserver', 'mkbase311_5py3', 'alpine'),
                        'ComposeMediaKrakenTraefik': ('mktraefik', 'alpine:3.11', 'alpine'),
                        'ComposeMediaKrakenTVHeadend': ('mktvheadend', 'lsiobase/alpine:3.10', 'alpine'),
                        'ComposeMediaKrakenWebSanic': ('mkwebappsanic', 'mkbase311_5py3', 'alpine'),
                        'ComposeMediaKrakenWebServer': ('mkwebappdeb', 'mkbasedeb10_2py3', 'debian'),
                        }

# these are for security and linting all code
# directory, name, base image, build script
STAGE_ONE_SECURITY_TOOLS = {'hadolint': ('mkhadolint', 'debian:stretch-slim '),
                            'kali': ('mkkali', 'kalilinux/kali-linux-docker', './build.sh'),
                            'sitadel': ('mksitadel', 'python:3'),
                            'testssl': ('mktestssl', 'alpine:3.9'),
                            'trivy': ('mktrivy', 'alpine:3.11'),
                            }

STAGE_TWO_SECURITY_TOOLS = {'rapidscan': ('mkrapidscan', 'mkkali'),
                            }

STAGE_ONE_TESTING_TOOLS = {'elk': ('mkelk', 'phusion/baseimage:0.11'),
                           'filebeat': ('mkfilebeat', 'docker.elastic.co/beats/filebeat:7.5.2'),
                           'fuxploider': ('mkfuxploider', 'python:3.6-alpine'),
                           'jenkins': ('mkjenkins', 'jenkins/jenkins:lts'),
                           'joxit_ui': ('mkjoxitui', 'node:10-alpine'),
                           'logspout': ('mklogspout', 'alpine:3.9'),
                           'metricbeat': ('mkmetricbeat', 'docker.elastic.co/beats/metricbeat:7.6.0'),
                           'pgadmin4': ('mkpgadmin', 'python:alpine3.9'),
                           'pghero': ('mkpghero', 'ruby:2.6.3-alpine3.9'),
                           'pgbouncerhero': ('mkpgbouncerhero', 'ruby:2.6.3'),
                           'metasploit': ('mkmetasploit', 'metasploitframework/metasploit-framework'),
                           'nikto': ('mknikto', 'alpine:3.10'),
                           'raccoon': ('mkraccoon', 'python:3.5-alpine'),
                           'registry': ('mkregistry', 'alpine:3.8'),
                           'testcode': ('mktestcode', 'mkbase311_5py3'),
                           'testwebapp': ('mktestwebapp', 'mkbase311_3py3'),
                           'vuls': ('mkvuls', 'golang:alpine'),
                           'wireshark': ('mkwireshark', 'debian:stretch-slim'),
                           }

STAGE_TWO_TESTING_TOOLS = {
}

STAGE_ONE_FS = {
    'ComposeMediaKrakenMooseFSChunkServer': ('mkmoosechunkserver', 'debian:strech', 'debian'),
    'ComposeMediaKrakenMooseFSChunkServerClient': (
        'mkmoosechunkserverclient', 'debian:strech', 'debian'),
    'ComposeMediaKrakenMooseFSClient': ('mkmooseclient', 'debian:strech', 'debian'),
    'ComposeMediaKrakenMooseFSMaster': ('mkmoosemaster', 'debian:strech', 'debian'),
}
