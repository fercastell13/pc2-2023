# ./auto.sh

# Ejecutar desde la carpeta de DockerCompose
# En caso de no tener permisos de escritura, ejecutar en linux:
# chmod +x auto.sh
# o en windows:
# icacls auto.sh /grant "usrname:RX"

# Construir las imágenes
docker build -t product-page -f ./ProductPage/Dockerfile .
# docker build -t details -f ./Ratings/Dockerfile .
# docker build -t details -f ./Reviews/Dockerfile .
# docker build -t details -f ./Ratings/Dockerfile .

# Lanzar los contenedores con Docker Compose
docker-compose up