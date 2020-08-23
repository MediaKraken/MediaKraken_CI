FROM docker.elastic.co/beats/filebeat:7.2.1
COPY filebeat.yml /usr/share/filebeat/
COPY modules.d /usr/share/filebeat/modules.d
USER root
CMD ["filebeat", "-e", "-strict.perms=false"]
