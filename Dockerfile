# Usar la imagen base de Python
FROM python:3.7.7-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY ./practica_creativa2/bookinfo/src/productpage /app

# Instalar dependencias
RUN pip install -r requirements.txt

# Exponer el puerto 9080
EXPOSE 9080

# Variable de entorno para el número de grupo
ENV GRUPO_NUMERO=21

# Comando para iniciar la aplicación
CMD ["python3", "productpage_monolith.py", "9080"]


# TODO: http://localhost:9080/productpage NO FUNCIONA

# PASOS A SEGUIR:
# 1.- Crear la imagen con la siguiente orden:
#       
# 2.- Arrancar el contenedor ene l puerto 9080
#      
# 3.- Abrir el navegador:

# 1.- $ docker build -t g21/product-page .
# 2.- $ docker run --name g21-product-page -p 9080:9080 -d g21/product-page
# 3.- $ htpp://localhost:9080/productpage