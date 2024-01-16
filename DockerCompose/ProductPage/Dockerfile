# /DockerCompose/ProductPage/Dockerfile

FROM python:3.7.7-slim

RUN apt-get update
RUN apt-get install -y python3-pip git

# Clonamos el repositorio
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2

# Instalacion de librerias (requirements.txt)
RUN pip3 install -r /practica_creativa2/bookinfo/src/productpage/requirements.txt

# Exponemos el puerto
EXPOSE 9080




# Si queremos construir la imagen usaremos
# el siguiente comando:
#       $ docker build -t product-page -f ./DockerCompose/ProductPage/Dockerfile .
#       $ docker run --name product-page -p 9080:9080 -d product-page
#       $ http://localhost:9080/product-page