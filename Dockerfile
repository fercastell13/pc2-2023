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
