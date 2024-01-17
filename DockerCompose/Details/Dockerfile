FROM ruby:2.7.1-slim
# COPY practica_creativa2/bookinfo/src/details/details.rb /opt/microservices/
COPY ./Details/details.rb /opt/microservices/

ENV SERVICE_VERSION=v1
ENV ENABLE_EXTERNAL_BOOK_SERVICE=true

EXPOSE 9080
CMD ["ruby", "/opt/microservices/details.rb", "9080"]

# Si queremos construir la imagen usaremos
# el siguiente comando:
#       $ docker build -t details -f ./DockerCompose/Details/Dockerfile .

# docker cp <CONTAINER_ID>:/ruta/a/details.rb ./Details/