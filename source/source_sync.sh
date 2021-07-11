#!/bin/sh
# bulk tmdb net fetch RUST
cp ../../source_rust/mk_lib_common/src/mk_lib_common.rs ../../docker/core/tmdb_netfetch_bulk/src/.
cp ../../source_rust/mk_lib_common/src/mk_lib_common_enum_media_type.rs ../../docker/core/tmdb_netfetch_bulk/src/.
cp ../../source_rust/mk_lib_compression/src/mk_lib_compression.rs ../../docker/core/tmdb_netfetch_bulk/src/.
cp ../../source_rust/mk_lib_database/src/mk_lib_database.rs ../../docker/core/tmdb_netfetch_bulk/src/.
cp ../../source_rust/mk_lib_database/src/mk_lib_database_download.rs ../../docker/core/tmdb_netfetch_bulk/src/.
cp ../../source_rust/mk_lib_database/src/mk_lib_database_metadata.rs ../../docker/core/tmdb_netfetch_bulk/src/.
cp ../../source_rust/mk_lib_logging/src/mk_lib_logging.rs ../../docker/core/tmdb_netfetch_bulk/src/.
cp ../../source_rust/mk_lib_network/src/mk_lib_network.rs ../../docker/core/tmdb_netfetch_bulk/src/.

# update tmdb net fetch RUST
cp ../../source_rust/mk_lib_common/src/mk_lib_common.rs ../../docker/core/tmdb_netfetch_update/src/.
cp ../../source_rust/mk_lib_common/src/mk_lib_common_enum_media_type.rs ../../docker/core/tmdb_netfetch_update/src/.
cp ../../source_rust/mk_lib_compression/src/mk_lib_compression.rs ../../docker/core/tmdb_netfetch_update/src/.
cp ../../source_rust/mk_lib_database/src/mk_lib_database.rs ../../docker/core/tmdb_netfetch_update/src/.
cp ../../source_rust/mk_lib_database/src/mk_lib_database_download.rs ../../docker/core/tmdb_netfetch_update/src/.
cp ../../source_rust/mk_lib_database/src/mk_lib_database_metadata.rs ../../docker/core/tmdb_netfetch_update/src/.
cp ../../source_rust/mk_lib_logging/src/mk_lib_logging.rs ../../docker/core/tmdb_netfetch_update/src/.
cp ../../source_rust/mk_lib_network/src/mk_lib_network.rs ../../docker/core/tmdb_netfetch_update/src/.

# cron RUST
cp ../../source_rust/mk_lib_logging/src/mk_lib_logging.rs ../../docker/core/cron_processor/src/.
cp ../../source_rust/mk_lib_database/src/mk_lib_database.rs ../../docker/core/cron_processor/src/.
cp ../../source_rust/mk_lib_database/src/mk_lib_database_cron.rs ../../docker/core/cron_processor/src/.

# device scanner
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenDevicescan/src/.
cp ../../source/main_hardware_discover.py ../../docker/alpine/ComposeMediaKrakenDevicescan/src/.

# download rust
cp ../../source_rust/mk_lib_logging/src/mk_lib_logging.rs ../../docker/core/download_server/src/.
cp ../../source_rust/mk_lib_network/src/mk_lib_network.rs ../../docker/core/download_server/src/.

# file system media scanner rust
cp ../../source_rust/mk_lib_logging/src/mk_lib_logging.rs ../../docker/core/file_system_media_scanner/src/.
cp ../../source_rust/mk_lib_network/src/mk_lib_network.rs ../../docker/core/file_system_media_scanner/src/.

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
cp ../../source_rust/mk_lib_logging/src/mk_lib_logging.rs ../../docker/core/file_system_inotify/src/.
cp ../../source_rust/mk_lib_database/src/mk_lib_database.rs ../../docker/core/file_system_inotify/src/.
cp ../../source_rust/mk_lib_database/src/mk_lib_database_library.rs ../../docker/core/file_system_inotify/src/.

# libretro core download
cp ../../source_rust/mk_lib_file/src/mk_lib_file.rs ../../docker/core/libretro_core_netfetch/src/.
cp ../../source_rust/mk_lib_hash/src/mk_lib_hash_md5.rs ../../docker/core/libretro_core_netfetch/src/.
cp ../../source_rust/mk_lib_logging/src/mk_lib_logging.rs ../../docker/core/libretro_core_netfetch/src/.
cp ../../source_rust/mk_lib_network/src/mk_lib_network.rs ../../docker/core/libretro_core_netfetch/src/.

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

# TEST reqwest RUST
cp ../../source_rust/mk_lib_compression/src/mk_lib_compression.rs ../../docker/rust/ComposeMediaKrakenTESTReqwestRust/src/.
cp ../../source_rust/mk_lib_network/src/mk_lib_network.rs ../../docker/rust/ComposeMediaKrakenTESTReqwestRust/src/.

# transcode
cp -R ../../source/common ../../docker/alpine/ComposeMediaKrakenTranscode/src/.
cp -R ../../source/database_async ../../docker/alpine/ComposeMediaKrakenTranscode/src/.
cp ../../source/async_transcode.py ../../docker/alpine/ComposeMediaKrakenTranscode/src/.
cp ../../source/castpy/cast.py ../../docker/alpine/ComposeMediaKrakenTranscode/src/.

# webserver
cp -R ../../source/common ../../docker/core/web_application/src/.
cp -R ../../source/database_async ../../docker/core/web_application/src/.
cp -R ../../source/network ../../docker/core/web_application/src/.
cp -R ../../source/web_app_sanic ../../docker/core/web_application/src/.
