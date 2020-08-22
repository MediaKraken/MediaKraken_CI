FROM docker.elastic.co/beats/filebeat:7.9.0
COPY filebeat.yml /usr/share/filebeat/
USER root
CMD ["filebeat", "-e", "-strict.perms=false"]
