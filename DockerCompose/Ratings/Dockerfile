FROM node:12.18.1-slim
WORKDIR /opt/microservices
COPY package.json ratings.js /opt/microservices/
ENV SERVICE_VERSION=v1
RUN npm install
EXPOSE 9080
CMD ["node", "ratings.js", "9080"]


# Si queremos construir la imagen usaremos
# el siguiente comando:
#       $ docker build -t details -f ./DockerCompose/Ratings/Dockerfile .