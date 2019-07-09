#!/bin/sh
docker run -d \
  -p 5050:5000 \
  --restart=always \
  --name mkregistry \
  -v /mnt/registry:/var/lib/registry \
  mkregistry:dev