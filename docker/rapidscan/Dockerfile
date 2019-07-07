# Download base image
FROM mediakraken/mkkali:dev

LABEL AUTHOR="Quinn D Granfor, spootdev@gmail.com"
LABEL Description="This image holds the rapidscan app"

# create work dir
RUN mkdir /mediakraken

COPY rapidscan.py /mediakraken
WORKDIR /mediakraken

CMD ["python /mediakraken/rapidscan.py"]
