# CDPS 2023
#  Práctica creativa 2
# Grupo 21

# TODO: http://localhost:9080/productpage NO FUNCIONA
# 1. Creamos la imagen:
    # $docker build -t g40/product-page .
# 2. Arrancamos el contenedor con el puerto 9080
    # $docker run --name g40-product-page -p 9080:9080 -e GROUP_NUMBER=40 -d g40/product-page
# 3. Abrimos el navegador: http://localhost:9080/productpage

# Es importante tener en cuenta que, al utilizar un solo contenedor para todos los servicios, 
# es posible que sea más difícil actualizar o cambiar la versión de un servicio específico sin 
# tener que volver a construir e instalar la imagen completa. Además, puede ser más difícil aislar
# y solucionar problemas en un servicio específico si todos están incluidos en un mismo contenedor.
# En general, se recomienda utilizar microservicios para facilitar el despliegue y el mantenimiento 
# de aplicaciones complejas.


# Utiliza una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo
WORKDIR /app

# Clona tu repositorio o copia los archivos necesarios
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git .

# Instala las dependencias
# RUN pip install -r ./practica_creativa2/bookinfo/src/productpage/requirements.txt

# Copia los archivos necesarios
COPY . /app

# Define la variable de entorno GRUPO_NUMERO
ENV GRUPO_NUMERO=21

# Se pone a escuchar el puerto 9080
EXPOSE 9080

# Ejecutar la aplicación
CMD ["python3", "./practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "9080"]