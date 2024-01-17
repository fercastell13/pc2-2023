# ./auto.sh

# En caso de no tener permisos de escritura, ejecutar en linux:
# chmod +x auto.sh
# o en windows:
# icacls auto.sh /grant "usrname:RX"

# Construir las imágenes
docker build -t product-page -f ./DockerCompose/ProductPage/Dockerfile .
docker build -t details -f ./DockerCompose/Ratings/Dockerfile .
docker build -t details -f ./DockerCompose/Reviews/Dockerfile .
docker build -t details -f ./DockerCompose/Ratings/Dockerfile .

# Lanzar los contenedores con Docker Compose
docker-compose up