# ./auto-docker.sh

# Ejecutar desde la carpeta de DockerCompose
# En caso de no tener permisos de escritura, ejecutar en linux:
# chmod +x aut-docker.sh
# o en windows:
# icacls auto-docker.sh /grant "usrname:RX"

# Construir las imágenes
# PASOS A SEGUIR:
# 1.- Crear la imagen con la siguiente orden:
docker build -t 21/product-page .
# 2.- Arrancar el contenedor ene l puerto 9080
docker run --name 21-product-page -p 9080:9080 -d 21/product-page
# 3.- Abrir el navegador:
# 3.- $ http://localhost:9080/productpage

# si falla el container y hay que reiniciar
# docker rm -f "containerID"