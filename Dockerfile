# Imagen disponible en DockerHub:
# https://hub.docker.com/repository/docker/fernandocastell/product-page/
# 

# Usar la imagen base de Python

FROM python:3.7.7-slim


# Instalaciones necesarias (pip y git)
RUN apt-get update
RUN apt-get install -y python3-pip git

COPY . /app
# Establecer el directorio de trabajo
WORKDIR /app

RUN rm -rf /app/*
# Copiar los archivos necesarios al contenedor
# COPY ./practica_creativa2/bookinfo/src/productpage /app
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2


# Instalar dependencias de requirements.txt
RUN pip install -r ./practica_creativa2/bookinfo/src/productpage/requirements.txt

# Abrir el puerto 9080, 
# donde se va a desplegar el servicio
EXPOSE 9080

# Variable de entorno para el número de grupo
ENV GRUPO_NUMERO=21

RUN sed -i "s/Simple Bookstore App/$GRUPO_NUMERO/g" ./practica_creativa2/bookinfo/src/productpage/templates/productpage.html



# Comando para iniciar la aplicación
CMD ["python3", "./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", "9080"]


# TODO: http://localhost:9080/productpage NO FUNCIONA

# PASOS A SEGUIR:
# 1.- Crear la imagen con la siguiente orden:
#       
# 2.- Arrancar el contenedor ene l puerto 9080
#      
# 3.- Abrir el navegador:

# 1.- $ docker build -t 21/product-page .
# 2.- $ docker run --name 21-product-page -p 9080:9080 -d 21/product-page
# 3.- $ http://localhost:9080/product-page

# si falla el container y hay que reiniciar
# docker rm -f "containerID"