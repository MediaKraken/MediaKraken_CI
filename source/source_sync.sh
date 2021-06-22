#!/bin/sh
# bulk tmdb net fetch RUST
cp ../../source_rust/mk_lib_common/src/mk_lib_common.rs ../../docker/rust/bulk_themoviedb_netfetch/src/.
cp ../../source_rust/mk_lib_common_enum_media_type/src/mk_lib_common_enum_media_type.rs ../../docker/rust/bulk_themoviedb_netfetch/src/.
cp ../../source_rust/mk_lib_compression/src/mk_lib_compression.rs ../../docker/rust/bulk_themoviedb_netfetch/src/.
cp ../../source_rust/mk_lib_database/src/mk_lib_database.rs ../../docker/rust/bulk_themoviedb_netfetch/src/.
cp ../../source_rust/mk_lib_database_download/src/mk_lib_database_download.rs ../../docker/rust/bulk_themoviedb_netfetch/src/.
cp ../../source_rust/mk_lib_database_metadata/src/mk_lib_database_metadata.rs ../../docker/rust/bulk_themoviedb_netfetch/src/.
cp ../../source_rust/mk_lib_logging/src/mk_lib_logging.rs ../../docker/rust/bulk_themoviedb_netfetch/src/.
cp ../../source_rust/mk_lib_networks/src/mk_lib_networks.rs ../../docker/rust/bulk_themoviedb_netfetch/src/.

# cron RUST
cp ../../source_rust/mk_lib_logging/src/mk_lib_logging.rs ../../docker/rust/ComposeMediaKrakenCronRust/src/.
cp ../../source_rust/mk_lib_database/src/mk_lib_database.rs ../../docker/rust/ComposeMediaKrakenCronRust/src/.
cp ../../source_rust/mk_lib_database/src/mk_lib_database_cron.rs ../../docker/rust/ComposeMediaKrakenCronRust/src/.

# devicescanner
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenDevicescan/src/.
cp ../../source/main_hardware_discover.py ../../docker/alpine/ComposeMediaKrakenDevicescan/src/.

# download
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenDownload/src/.
cp -R ../../source/database ../../docker/alpine/ComposeMediaKrakenDownload/src/.
cp -R ../../source/network ../../docker/alpine/ComposeMediaKrakenDownload/src/.
cp ../../source/main_download.py ../../docker/alpine/ComposeMediaKrakenDownload/src/.

# load game/metadata
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenGameData/src/.
cp -R ../../source/database ../../docker/alpine/ComposeMediaKrakenGameData/src/.
cp ../../source/subprogram_metadata_games.py ../../docker/alpine/ComposeMediaKrakenGameData/src/.

# hardware
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenHardware/src/.
cp -R ../../source/database ../../docker/alpine/ComposeMediaKrakenHardware/src/.
cp -R ../../source/network ../../docker/alpine/ComposeMediaKrakenHardware/src/.
cp ../../source/main_hardware.py ../../docker/alpine/ComposeMediaKrakenHardware/src/.

# inotify rust
cp ../../source_rust/mk_lib_logging/src/mk_lib_logging.rs ../../docker/rust/ComposeMediaKrakenInotifyRust/src/.
cp ../../source_rust/mk_lib_database/src/mk_lib_database.rs ../../docker/rust/ComposeMediaKrakenInotifyRust/src/.
cp ../../source_rust/mk_lib_database/src/mk_lib_database_library.rs ../../docker/rust/ComposeMediaKrakenInotifyRust/src/.

# metadata
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenMetadata/src/.
cp -R ../../source/database_async ../../docker/alpine/ComposeMediaKrakenMetadata/src/.
cp -R ../../source/metadata ../../docker/alpine/ComposeMediaKrakenMetadata/src/.
cp ../../source/main_server_metadata_api.py ../../docker/alpine/ComposeMediaKrakenMetadata/src/.
cp ../../source/main_server_metadata_api_worker.py ../../docker/alpine/ComposeMediaKrakenMetadata/src/.
cp ../../source/subprogram*.py ../../docker/alpine/ComposeMediaKrakenMetadata/src/.
cp ../../source/async*.py ../../docker/alpine/ComposeMediaKrakenMetadata/src/.

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
cp ../../source/main_reactor_line.py  ../../docker/alpine/ComposeMediaKrakenReactor/src/.
cp ../../source/db_create_update.py ../../docker/alpine/ComposeMediaKrakenReactor/src/.
cp ../../source/db_update_version.py ../../docker/alpine/ComposeMediaKrakenReactor/src/.
cp ../../source/main_server_link.py ../../docker/alpine/ComposeMediaKrakenReactor/src/.

# ripper
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenRipper/src/.
cp ../../source/main_ripper.py ../../docker/alpine/ComposeMediaKrakenRipper/src/.

# transcode
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenTranscode/src/.
cp -R ../../source/database_async ../../docker/alpine/ComposeMediaKrakenTranscode/src/.
cp ../../source/async_transcode.py ../../docker/alpine/ComposeMediaKrakenTranscode/src/.
cp ../../source/castpy/cast.py ../../docker/alpine/ComposeMediaKrakenTranscode/src/.

# webserver
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenWebSanic/src/.
cp -R ../../source/database_async ../../docker/alpine/ComposeMediaKrakenWebSanic/src/.
cp -R ../../source/network ../../docker/alpine/ComposeMediaKrakenWebSanic/src/.
cp -R ../../source/web_app_sanic ../../docker/alpine/ComposeMediaKrakenWebSanic/src/.
