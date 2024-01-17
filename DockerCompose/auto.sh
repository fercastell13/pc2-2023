# ./auto.sh

# Ejecutar desde la carpeta de DockerCompose
# En caso de no tener permisos de escritura, ejecutar en linux:
# chmod +x auto.sh
# o en windows:
# icacls auto.sh /grant "usrname:RX"

# Construir las imágenes
docker build -t productpage -f ./ProductPage/Dockerfile .
docker build -t details -f ./Details/Dockerfile .
# docker build -t details -f ./DockerCompose/Details/Dockerfile .
# docker build -t reviews -f ./Reviews/Dockerfile .
# docker build -t ratings -f ./Ratings/Dockerfile .

# Lanzar los contenedores con Docker Compose
docker-compose up