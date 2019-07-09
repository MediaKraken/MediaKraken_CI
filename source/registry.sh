#!/bin/sh
docker run -d \
  -p 5000:5000 \
  --restart=always \
  --name mkregistry \
  -v /mnt/registry:/var/lib/registry \
  registry:2