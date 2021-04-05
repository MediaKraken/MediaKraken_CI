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

# these are the base/unique game servers
STAGE_ONE_GAME_SERVERS = {
    'ComposeMediaKrakenBaseSteamCMD': ('mkbasesteamcmd', 'debian:10.9-slim', 'game_server'),
    'ComposeMediaKrakenBaseSteamCMDRoot': ('mkbasesteamcmdroot', 'debian:10.9-slim', 'game_server'),
    'ComposeMediaKrakenBaseWine': ('mkbasewine', 'ubuntu:20.10', 'game_server'),
    'ComposeMediaKrakenDosBoxWeb': ('mkdosboxweb', 'ubuntu:18.04', 'game_server'),
    #'ComposeMediaKrakenQ3A': ('mkgameq3a', 'alpine:3.13.3', 'game_server'),
    'ComposeMediaKrakenQuake2': ('mkgamequake2', 'mkgamequake2', 'game_server'),
    'ComposeMediaKrakenRetroArchWeb': ('mkretroarchweb', 'debian:buster', 'game_server'),
    'ComposeMediaKrakenUT2004': ('mkut2004', 'debian:jessie', 'game_server'),
    'ComposeMediaKrakenUT99': ('mkut99', 'i386/ubuntu:18.04', 'game_server'),
}

# depends on a base image from above
# https://developer.valvesoftware.com/wiki/Dedicated_Servers_List
STAGE_TWO_GAME_SERVERS = {
    # 'ComposeMediaKrakenQ3A_CPMA': ('mkgameq3a_cpma', 'mkgameq3a', 'game_server'),
    # 'ComposeMediaKrakenQ3A_OSP': ('mkgameq3a_osp', 'mkgameq3a', 'game_server'),
    # 'ComposeMediaKrakenQ3A_RQ3': ('mkgameq3a_rq3', 'mkgameq3a', 'game_server'),

    # 'ComposeMediaKrakenSteamCMD_7DaysToDie': ('mksteam_7d2d', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_AssettoCorsa': ('mksteam_assettocorsa', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Astroneer': ('mksteam_astroneer', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_AgeofChivalry': ('mksteam_ageofchivalry', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_AlienSwarm': ('mksteam_alienswarm', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_AlienSwarmReactiveDrop': ('mksteam_alienswarmrd', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_AliensvsPredator': ('mksteam_avsp', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_AmericasArmyProvingGrounds': ('mksteam_americasarymypg', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_ARK: Survival of the Fittest': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_ARKSurvivalEvolved': ('mksteam_arksurvivalevolved', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_ARMA2': ('mksteam_arma2', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Arma2: Operation Arrowhead': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_AmericasArmy3': ('mksteam_americasarmy3', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_BlackMesaDM': ('mksteam_blackmesadm', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_BladeSymphony': ('mksteam_bladesymphony', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_BlazeRush': ('mksteam_blazerush', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_BrainBread2': ('mksteam_braindead2', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Breach': ('mksteam_breach', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Brink': ('mksteam_brink', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Capsa': ('mksteam_capsa', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Call of Duty: Modern Warfare 3': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Chivalry: Deadliest Warrior': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_ChivalryMedievalWarfare': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Conan Exiles': ('mksteam_conanexiles', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Contagion': ('mksteam_contagion', 'mkbasewine', 'game_server'),
    'ComposeMediaKrakenSteamCMD_CSGO': ('mksteam_csgo', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_CounterStrike': ('mksteam_cs', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_CounterStrikeConditionZero': ('mksteam_cszero', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_CounterStrikeSource': ('mksteam_cssource', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_DIPRIP': ('mksteam_diprip', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Dark Horizons: Mechanized Corps': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Dark Messiah of Might & Magic': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Darkest Hour': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_DayofDefeat': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_DayofDefeatSource': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_DayofInfamy': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Deathmatch Classic': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Dino D-Day': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Dayz': ('mksteam_dayz', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_DontStarveTogether': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Dota2': ('mksteam_dota2', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Double Action': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Dystopia': ('mksteam_dystopia', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_EdenStar': ('mksteam_edenstar', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_EYE': ('mksteam_eye', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Empires': ('mksteam_empires', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_EternalSilence': ('mksteam_eternalsilence', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_FistfulofFrags': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_The Forest': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Fortress Forever': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_GarrysMod': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Half-Life 2: Deathmatch': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Half-Life Deathmatch': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_HalfLife': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_HalfLife: Opposing Force': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    'ComposeMediaKrakenSteamCMD_HoldfastNaW': ('mksteam_holdfastnaw', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Homefront': ('mksteam_homefront', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Hurtworld': ('mksteam_hurtworld', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Insurgency 2014': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Insurgency: Modern Infantry Combat': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_JustCause 2: Multiplayer': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_KillingFloor': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_KillingFloor2': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Kingdoms Rise': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Lambda Wars': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Left 4 Dead 2': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Left 4 Dead': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Life is Feudal': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Mare Nostrum': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Monday Night Combat': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    'ComposeMediaKrakenSteamCMD_Mordhau': ('mksteam_mordhau', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_NaturalSelection2': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Nexuiz': ('mksteam_nexuiz', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_NEOTOKYO': ('mksteam_neotokyo', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_No More Room In Hell': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_NS2: Combat': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Nuclear Dawn': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_OutofReach': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Painkiller Hell & Damnation': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Pirates, Vikings, and Knights II': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Primal Carnage': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_ProjectZomboid': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_RACE07': ('mksteam_race07', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Ravaged': ('mksteam_ravaged', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_RedOrchestra': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Red Orchestra 2': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Reflex': ('mksteam_reflex', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Reign Of Kings': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Ricochet': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Rust': ('mksteam_rust', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Sven Co-op': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Serious Sam HD': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Serious Sam Classics: Revolution': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Serious Sam HD: The Second Encounter': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_SeriousSam3': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Sniper Elite 3': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Sniper Elite V2': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Space Engineers': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    'ComposeMediaKrakenSteamCMD_Squad': ('mksteam_squad', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Starbound': ('mksteam_starbound', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Starvoid': ('mksteam_starvoid', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_SvenCo-op': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Synergy': ('mksteam_synergy', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Takedown: Red Sabre': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Terraria': ('mksteam_terraria', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_TeamFortressClassic': ('mksteam_FAKE', 'mkbasesteamcmdroot', 'game_server'),
    'ComposeMediaKrakenSteamCMD_TF2': ('mksteam_tf2', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_The Haunted: Hells Reach': ('mksteam_FAKE', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_TheShip': ('mksteam_theship', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_TowerUnite': ('mksteam_towerunite', 'mkbasesteamcmdroot', 'game_server'),
    'ComposeMediaKrakenSteamCMD_Valheim': ('mksteam_valheim', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_Unturned': ('mksteam_unturned', 'mkbasesteamcmdroot', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_ZombieGrinder': ('mksteam_zombiegrinder', 'mkbasewine', 'game_server'),
    # 'ComposeMediaKrakenSteamCMD_ZombiePanic': ('mksteam_zombiepanic', 'mkbasesteamcmdroot', 'game_server'),

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
