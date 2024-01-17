# ./auto.sh

# Ejecutar desde la carpeta de DockerCompose
# En caso de no tener permisos de escritura, ejecutar en linux:
# chmod +x auto.sh
# o en windows:
# icacls auto.sh /grant "usrname:RX"

# Construir las imágenes
docker build -t 21/productpage -f ./ProductPage/Dockerfile .
docker build -t 21/details -f ./Details/Dockerfile .

# Para Reviews:
# copiar los ficheros de la aplicacion
# cambiar pwd por PWD en el siguiente comando: (powershell)
# docker run --rm -u root -v ${PWD}:/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build
docker build -t 21/reviews -f ./Reviews/reviews-wlpcfg/Dockerfile .

# docker build -t 21/reviews:v3 -f ./Reviews/reviews-wlpcfg/Dockerfile .



docker build -t 21/ratings -f ./Ratings/Dockerfile .

# Lanzar los contenedores con Docker Compose
docker-compose up