#!/bin/sh

# broadcast
cp ../../source/subprogram_broadcast.py ../../docker/alpine/ComposeMediaKrakenBroadcast/src/.
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenBroadcast/src/.

# cast images
cp ../../source/castpy/cast.py ../../docker/alpine/ComposeMediaKrakenCastImage/src/.

# cron
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenCron/src/.
cp -R ../../source/database ../../docker/alpine/ComposeMediaKrakenCron/src/.
cp -R ../../source/network ../../docker/alpine/ComposeMediaKrakenCron/src/.
cp ../../source/subprogram_cron_checker.py ../../docker/alpine/ComposeMediaKrakenCron/src/.

# devicescanner
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenDevicescan/src/.
cp ../../source/main_hardware_discover.py ../../docker/alpine/ComposeMediaKrakenDevicescan/src/.

# download
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenDownload/src/.
cp -R ../../source/database ../../docker/alpine/ComposeMediaKrakenDownload/src/.
cp -R ../../source/network ../../docker/alpine/ComposeMediaKrakenDownload/src/.
cp ../../source/main_download.py ../../docker/alpine/ComposeMediaKrakenDownload/src/.

# ffprobe
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenFFProbe/src/.
cp -R ../../source/database ../../docker/alpine/ComposeMediaKrakenFFProbe/src/.
cp ../../source/subprogram_ffprobe_metadata.py ../../docker/alpine/ComposeMediaKrakenFFProbe/src/.

# load game/metadata
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenGameData/src/.
cp -R ../../source/database ../../docker/alpine/ComposeMediaKrakenGameData/src/.
cp ../../source/subprogram_metadata_games.py ../../docker/alpine/ComposeMediaKrakenGameData/src/.

# hardware
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenHardware/src/.
cp -R ../../source/database ../../docker/alpine/ComposeMediaKrakenHardware/src/.
cp -R ../../source/network ../../docker/alpine/ComposeMediaKrakenHardware/src/.
cp ../../source/main_hardware.py ../../docker/alpine/ComposeMediaKrakenHardware/src/.

# metadata
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenMetadata/src/.
cp -R ../../source/database ../../docker/alpine/ComposeMediaKrakenMetadata/src/.
cp -R ../../source/metadata ../../docker/alpine/ComposeMediaKrakenMetadata/src/.
cp ../../source/main_server_metadata_api.py ../../docker/alpine/ComposeMediaKrakenMetadata/src/.
cp ../../source/main_server_metadata_api_worker.py ../../docker/alpine/ComposeMediaKrakenMetadata/src/.
cp ../../source/build_image_directory.py ../../docker/alpine/ComposeMediaKrakenMetadata/src/.
cp ../../source/build_trailer_directory.py ../../docker/alpine/ComposeMediaKrakenMetadata/src/.
cp ../../source/subprogram*.py ../../docker/alpine/ComposeMediaKrakenMetadata/src/.
cp ../../source/db_metadata_fix.py ../../docker/alpine/ComposeMediaKrakenMetadata/src/.
cp ../../source/bulk_themoviedb_netfetch.py ../../docker/alpine/ComposeMediaKrakenMetadata/src/.

# pika
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenPika/src/.
cp -R ../../source/database ../../docker/alpine/ComposeMediaKrakenPika/src/.
cp -R ../../source/network ../../docker/alpine/ComposeMediaKrakenPika/src/.
cp -R ../../source/metadata ../../docker/alpine/ComposeMediaKrakenPika/src/.
cp ../../source/subprogram*.py  ../../docker/alpine/ComposeMediaKrakenPika/src/.

# reactor
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenReactor/src/.
cp -R ../../source/database ../../docker/alpine/ComposeMediaKrakenReactor/src/.
cp -R ../../source/network ../../docker/alpine/ComposeMediaKrakenReactor/src/.
cp ../../source/subprogram*.py  ../../docker/alpine/ComposeMediaKrakenReactor/src/.

# ripper
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenRipper/src/.
cp ../../source/main_ripper.py ../../docker/alpine/ComposeMediaKrakenRipper/src/.

# roku thumb
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenRokuThumb/src/.
cp ../../source/subprogram_roku_thumbnail_generate.py ../../docker/alpine/ComposeMediaKrakenRokuThumb/src/.

# server
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenServer/src/.
cp -R ../../source/database ../../docker/alpine/ComposeMediaKrakenServer/src/.
cp -R ../../source/network ../../docker/alpine/ComposeMediaKrakenServer/src/.
cp ../../source/db_create_update.py ../../docker/alpine/ComposeMediaKrakenServer/src/.
cp ../../source/db_update_version.py ../../docker/alpine/ComposeMediaKrakenServer/src/.
cp ../../source/main_server.py ../../docker/alpine/ComposeMediaKrakenServer/src/.
cp ../../source/main_server_link.py ../../docker/alpine/ComposeMediaKrakenServer/src/.
cp ../../source/subprogram*.py  ../../docker/alpine/ComposeMediaKrakenServer/src/.

# slave
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenSlave/src/.
cp -R ../../source/database ../../docker/alpine/ComposeMediaKrakenSlave/src/.
cp ../../source/main_server_slave.py ../../docker/alpine/ComposeMediaKrakenSlave/src/.

# webserver - alpine sanic
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenWebSanic/src/.
cp -R ../../source/database_async ../../docker/alpine/ComposeMediaKrakenWebSanic/src/.
cp -R ../../source/network ../../docker/alpine/ComposeMediaKrakenWebSanic/src/.
cp -R ../../source/web_app_sanic ../../docker/alpine/ComposeMediaKrakenWebSanic/src/.
