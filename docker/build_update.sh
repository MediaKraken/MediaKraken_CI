git pull

cd clair
docker build -t mediakraken/mkclair .

cd ../elk
docker build -t mediakraken/mkelk .

cd ../jenkins
docker build -t mediakraken/mkjenkins .

cd ../pgadmin4
docker build -t mediakraken/mkpgadmin .

cd ../registry
docker build -t mediakraken/mkregistry .

cd ../sonarqube
docker build -t mediakraken/mksonarqube .

cd ../testssl
docker build -t mediakraken/mktestssl .

cd ../wireshark
docker build -t mediakraken/mkwireshark .
