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
ALPINE_MIRROR = 'dl-cdn.alpinelinux.org'

# PYPI_MIRROR = 'th-bandersnatch-1'
PYPI_MIRROR = 'pypi.python.org'

DOCKER_REPOSITORY = 'th-registry-1.beaverbay.local:5000'  # https://index.docker.io:443

PROXY_IP_PORT = '0.0.0.0:8080'
PROXY_USER_NAME = None
PROXY_USER_PASS = None

# the data is directory, name of container, base image used to build container

# base OS images to build off of, meaning there is a 'from' in the docker file(s) that use these
# or simply stand alone images
STAGE_ONE_IMAGES = {
    'ComposeMediaKrakenBase3133Py3': ('mkbase_alpinepy3', 'alpine:3.13.3', 'alpine'),
    'ComposeMediaKrakenBaseFFMPEG': ('mkbaseffmpeg', 'alpine:3.13.2', 'alpine'),
    'ComposeMediaKrakenBaseNodeJS': ('mkbasenode', 'alpine:3.13.2', 'alpine'),
    #'ComposeMediaKrakenBasePYPYAlpine': ('mkbasepypyalpine', '3.13.3', 'alpine'),
    'ComposeMediaKrakenBasePYPYDebian': ('mkbasepypydebian', 'debian:buster-slim', 'debian'),
}

# build on top of base os images from above
STAGE_TWO_IMAGES = {
    'ComposeMediaKrakenBaseNodeFFMPEG': ('mkbasenodeffmpeg', 'mkbaseffmpeg', 'alpine'),
    'ComposeMediaKrakenCastImage': ('mkcastimage', 'mkbase_alpinepy3', 'alpine'),
    'ComposeMediaKrakenDevicescan': ('mkdevicescan', 'mkbase_alpinepy3', 'alpine'),
    'ComposeMediaKrakenRipper': ('mkripper', 'mkbaseffmpeg', 'alpine'),
    # 'ComposeMediaKrakenSlave': ('mkslave', 'mkbasenodeffmpeg', 'alpine'),
    'ComposeMediaKrakenTwitchRecordUser': ('mktwitchrecorduser', 'mkbase_alpinepy3', 'alpine')}

# these are the final "compose" images
STAGE_COMPOSE_IMAGES = {
    'ComposeMediaKrakenBarman': ('mkbarman', 'debian:jessie', 'debian'),
    'ComposeMediaKrakenBroadcast': ('mkbroadcast', 'mkbase_alpinepy3', 'alpine'),
    # 'ComposeMediaKrakenConsul': ('mkconsul', 'alpine:3.9', 'alpine'),
    'ComposeMediaKrakenCron': ('mkcron', 'mkbase_alpinepy3', 'alpine'),
    'ComposeMediaKrakenDatabase13': ('mkdatabase', 'debian:buster-slim', 'debian'),
    'ComposeMediaKrakenDMS': ('mkdms', 'mkbaseffmpeg', 'alpine'),
    'ComposeMediaKrakenDownload': ('mkdownload', 'mkbase_alpinepy3', 'alpine'),
    'ComposeMediaKrakenGameData': ('mkgamedata', 'mkbase_alpinepy3', 'alpine'),
    # 'ComposeMediaKrakenHAProxy': ('mkpghaproxy', 'alpine:3.12', 'alpine'),
    'ComposeMediaKrakenHardware': ('mkhardware', 'mkbase_alpinepy3', 'alpine'),
    'ComposeMediaKrakenInotify': ('mkinotify', 'alpine:3.13.3', 'alpine'),
    'ComposeMediaKrakenLDAP': ('mkldap', 'lsiobase/alpine:3.11', 'alpine'),
    'ComposeMediaKrakenMetadata': ('mkmetadata', 'mkbase_alpinepy3', 'alpine'),
    # 'ComposeMediaKrakenMusicBrainz': ('mkmusicbrainz', 'lsiobase/alpine:3.6', 'alpine'),
    'ComposeMediaKrakenNginx': ('mknginx', 'alpine:3.10', 'alpine'),
    # 'ComposeMediaKrakenNginxPagespeed': ('mknginxpagespeed', 'alpine:3.8', 'alpine'),
    'ComposeMediaKrakenPGBouncer': ('mkpgbouncer', 'alpine:3.13.3', 'alpine'),
    'ComposeMediaKrakenPika': ('mkpika', 'mkbase_alpinepy3', 'alpine'),
    'ComposeMediaKrakenRabbitMQ': ('mkrabbitmq', 'alpine:3.11', 'alpine'),
    'ComposeMediaKrakenReactor': ('mkreactor', 'mkbase_alpinepy3', 'alpine'),
    'ComposeMediaKrakenServer': ('mkserver', 'mkbase_alpinepy3', 'alpine'),
    'ComposeMediaKrakenTeamspeak': ('mkteamspeak', 'alpine:3.8', 'alpine'),
    'ComposeMediaKrakenTranscode': ('mktranscode', 'mkbaseffmpeg', 'alpine'),
    'ComposeMediaKrakenTransmission': ('mktransmission', 'alpine:3.13.3', 'alpine'),
    # 'ComposeMediaKrakenTraefik': ('mktraefik', 'alpine:3.11', 'alpine'),
    'ComposeMediaKrakenTVHeadend': ('mktvheadend', 'lsiobase/alpine:3.12', 'alpine'),
    'ComposeMediaKrakenWebSanic': ('mkwebappsanic', 'mkbase_alpinepy3', 'alpine'),
}

# these are the game servers
STAGE_ONE_GAME_SERVERS = {
    'ComposeMediaKrakenBaseSteamCMD': ('mkbasesteamcmd', 'debian:10.3-slim', 'game_server'),
    'ComposeMediaKrakenDosBoxWeb': ('mkdosboxweb', 'ubuntu:18.04', 'game_server'),
    'ComposeMediaKrakenRetroArchWeb': ('mkretroarchweb', 'debian:buster', 'game_server'),
}

STAGE_TWO_GAME_SERVERS = {}

# these are for security and linting all code
# directory, name, base image, build script
STAGE_ONE_SECURITY_TOOLS = {
}

STAGE_TWO_SECURITY_TOOLS = {
}

STAGE_ONE_TESTING_TOOLS = {
    'elk': ('mkelk', 'phusion/baseimage:18.04-1.0.0'),
    'filebeat': ('mkfilebeat', 'docker.elastic.co/beats/filebeat:7.5.2'),
    'jenkins': ('mkjenkins', 'jenkins/jenkins:lts'),
    'joxit_ui': ('mkjoxitui', 'node:10-alpine'),
    'logspout': ('mklogspout', 'alpine:3.9'),
    'metricbeat': ('mkmetricbeat', 'docker.elastic.co/beats/metricbeat:7.6.0'),
    'pgadmin4': ('mkpgadmin', 'python:alpine3.9'),
    'registry': ('mkregistry', 'alpine:3.8'),
    'testwebapp': ('mktestwebapp', 'mkbase_alpinepy3'),
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
