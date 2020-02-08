FROM docker.elastic.co/beats/filebeat:7.5.2
COPY filebeat.yml /usr/share/filebeat/
USER root
RUN chown filebeat /usr/share/filebeat/filebeat.yml \
     && chmod go-w /usr/share/filebeat/filebeat.yml
USER filebeat
CMD ["filebeat", "-e", "-strict.perms=false"]
