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

# TODO
# 'ComposeMediaKrakenDMS': ('mkdms', 'mkbaseffmpeg', 'alpine'), - dlna
# 'ComposeMediaKrakenBasePYPYAlpine': ('mkbasepypyalpine', '3.13.3', 'alpine'), - most images are alpine
# 'ComposeMediaKrakenMusicBrainz': ('mkmusicbrainz', 'lsiobase/alpine:3.6', 'alpine'), - use official image
# 'ComposeMediaKrakenNginxPagespeed': ('mknginxpagespeed', 'alpine:3.8', 'alpine'), pagespeed is suppossed to help speed

# Not needed
# 'ComposeMediaKrakenSlave': ('mkslave', 'mkbasenodeffmpeg', 'alpine'),
# 'ComposeMediaKrakenConsul': ('mkconsul', 'alpine:3.9', 'alpine'),
# 'ComposeMediaKrakenHAProxy': ('mkpghaproxy', 'alpine:3.12', 'alpine'),
# 'ComposeMediaKrakenTraefik': ('mktraefik', 'alpine:3.11', 'alpine'),

# the data is directory, name of container, base image used to build container

# base OS images to build off of, meaning there is a 'from' in the docker file(s) that use these
# or simply stand alone images
STAGE_ONE_IMAGES = {
    'ComposeMediaKrakenBase3133Py3': ('mkbase_alpinepy3', 'alpine:3.13.3', 'alpine'),
    'ComposeMediaKrakenBaseFFMPEG': ('mkbaseffmpeg', 'alpine:3.13.2', 'alpine'),
    'ComposeMediaKrakenBaseNodeJS': ('mkbasenode', 'alpine:3.13.2', 'alpine'),
    'ComposeMediaKrakenBasePYPYDebian': ('mkbasepypydebian', 'debian:buster-slim', 'debian'),
}

# build on top of base os images from above
STAGE_TWO_IMAGES = {
    'ComposeMediaKrakenBaseNodeFFMPEG': ('mkbasenodeffmpeg', 'mkbaseffmpeg', 'alpine'),
    'ComposeMediaKrakenCastImage': ('mkcastimage', 'mkbase_alpinepy3', 'alpine'),
    'ComposeMediaKrakenDevicescan': ('mkdevicescan', 'mkbase_alpinepy3', 'alpine'),
    'ComposeMediaKrakenRipper': ('mkripper', 'mkbaseffmpeg', 'alpine'),
    'ComposeMediaKrakenTwitchRecordUser': ('mktwitchrecorduser', 'mkbase_alpinepy3', 'alpine')}

# these are the final "compose" images
STAGE_COMPOSE_IMAGES = {
    'ComposeMediaKrakenBarman': ('mkbarman', 'debian:jessie', 'debian'),
    'ComposeMediaKrakenBroadcast': ('mkbroadcast', 'mkbase_alpinepy3', 'alpine'),
    'ComposeMediaKrakenCron': ('mkcron', 'mkbase_alpinepy3', 'alpine'),
    'ComposeMediaKrakenDatabase13': ('mkdatabase', 'debian:buster-slim', 'debian'),
    'ComposeMediaKrakenDownload': ('mkdownload', 'mkbase_alpinepy3', 'alpine'),
    'ComposeMediaKrakenGameData': ('mkgamedata', 'mkbase_alpinepy3', 'alpine'),
    'ComposeMediaKrakenHardware': ('mkhardware', 'mkbase_alpinepy3', 'alpine'),
    'ComposeMediaKrakenInotify': ('mkinotify', 'alpine:3.13.3', 'alpine'),
    'ComposeMediaKrakenLDAP': ('mkldap', 'lsiobase/alpine:3.11', 'alpine'),
    'ComposeMediaKrakenMetadata': ('mkmetadata', 'mkbase_alpinepy3', 'alpine'),
    'ComposeMediaKrakenNginx': ('mknginx', 'alpine:3.10', 'alpine'),
    'ComposeMediaKrakenPGBouncer': ('mkpgbouncer', 'alpine:3.13.3', 'alpine'),
    'ComposeMediaKrakenPika': ('mkpika', 'mkbase_alpinepy3', 'alpine'),
    'ComposeMediaKrakenRabbitMQ': ('mkrabbitmq', 'alpine:3.11', 'alpine'),
    'ComposeMediaKrakenReactor': ('mkreactor', 'mkbase_alpinepy3', 'alpine'),
    'ComposeMediaKrakenServer': ('mkserver', 'mkbase_alpinepy3', 'alpine'),
    'ComposeMediaKrakenTeamspeak': ('mkteamspeak', 'alpine:3.8', 'alpine'),
    'ComposeMediaKrakenTranscode': ('mktranscode', 'mkbaseffmpeg', 'alpine'),
    'ComposeMediaKrakenTransmission': ('mktransmission', 'alpine:3.13.3', 'alpine'),
    'ComposeMediaKrakenTVHeadend': ('mktvheadend', 'lsiobase/alpine:3.12', 'alpine'),
    'ComposeMediaKrakenWebSanic': ('mkwebappsanic', 'mkbase_alpinepy3', 'alpine'),
}

# these are the base game servers
STAGE_ONE_GAME_SERVERS = {
    'ComposeMediaKrakenBaseSteamCMD': ('mkbasesteamcmd', 'debian:10.9-slim', 'game_server'),
    'ComposeMediaKrakenBaseSteamCMDRoot': ('mkbasesteamcmdroot', 'debian:10.9-slim', 'game_server'),
    'ComposeMediaKrakenDosBoxWeb': ('mkdosboxweb', 'ubuntu:18.04', 'game_server'),
    #'ComposeMediaKrakenQ3A': ('mkgameq3a', 'alpine:3.13.3', 'game_server'),
    'ComposeMediaKrakenRetroArchWeb': ('mkretroarchweb', 'debian:buster', 'game_server'),
}

STAGE_TWO_GAME_SERVERS = {
    'ComposeMediaKrakenSteamCMDCSGO': ('mksteamcsgo', 'mkbasesteamcmdroot', 'game_server'),
    'ComposeMediaKrakenSteamCMDHoldfastNaW': ('mksteamholdfastnaw', 'mkbasesteamcmdroot', 'game_server'),
    'ComposeMediaKrakenSteamCMDMordhau': ('mksteammordhau', 'mkbasesteamcmdroot', 'game_server'),
    'ComposeMediaKrakenSteamCMDSquad': ('mksteamsquad', 'mkbasesteamcmdroot', 'game_server'),
    'ComposeMediaKrakenSteamCMDTF2': ('mksteamtf2', 'mkbasesteamcmdroot', 'game_server'),
    'ComposeMediaKrakenSteamCMDValheim': ('mksteamvalheim', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenQ3A_CPMA': ('mkgameq3a_cpma', 'mkgameq3a', 'game_server'),
    # 'ComposeMediaKrakenQ3A_OSP': ('mkgameq3a_osp', 'mkgameq3a', 'game_server'),
    # 'ComposeMediaKrakenQ3A_RQ3': ('mkgameq3a_rq3', 'mkgameq3a', 'game_server'),
}

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
    'ComposeMediaKrakenMooseFSChunkServerClient': ('mkmoosechunkserverclient', 'debian:strech', 'debian'),
    'ComposeMediaKrakenMooseFSClient': ('mkmooseclient', 'debian:strech', 'debian'),
    'ComposeMediaKrakenMooseFSMaster': ('mkmoosemaster', 'debian:strech', 'debian'),
}
