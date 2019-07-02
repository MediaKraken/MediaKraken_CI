git pull

cd ../clair
docker build -t mediakraken/mkclair .

cd ../jenkins
docker build -t mediakraken/mkjenkins .

cd ../sonarqube
docker build -t mediakraken/mksonarqube .

cd ../testssl
docker build -t mediakraken/mktestssl .
