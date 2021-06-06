FROM clojure:openjdk-11-lein as build-env

ADD . /app
WORKDIR /app

RUN lein uberjar

# -----------------------------------------------------------------------------

from openjdk:11

RUN groupadd -r meuse && useradd -r -s /bin/false -g meuse meuse
RUN mkdir /app
COPY --from=build-env /app/target/uberjar/meuse-*-standalone.jar /app/meuse.jar

RUN chown -R meuse:meuse /app

RUN apt-get update && apt-get -y upgrade && apt-get install -y git

RUN mkdir /mediakraken && mkdir /mediakraken/cargo
COPY meuse.cfg /mediakraken/meuse.cfg
COPY config.json /mediakraken/cargo/config.json

user meuse

ENTRYPOINT ["java"]

CMD ["-jar", "/app/meuse.jar"]
