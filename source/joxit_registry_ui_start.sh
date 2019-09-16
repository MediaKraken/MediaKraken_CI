docker run -d -p 8000:80 -e REGISTRY_URL=th-registry-1.beaverbay.local:5000 -e DELETE_IMAGES=true th-registry-1.beaverbay.local:5000/mediakraken/mkjoxitui:dev

docker run -d   -p 5000:5000   --restart=always   --name mkregistry   -v /mnt/registry:/var/lib/registry   registry:2
