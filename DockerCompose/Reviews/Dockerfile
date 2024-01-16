FROM openjdk:8-jre-slim
WORKDIR /opt/microservices
COPY build/libs/reviews.jar /opt/microservices/
ENV SERVICE_VERSION=v1
EXPOSE 9080
CMD ["java", "-jar", "reviews.jar"]


# Si queremos construir la imagen usaremos
# el siguiente comando:
#       $ docker build -t details -f ./DockerCompose/Reviews/Dockerfile .

# $ docker run --rm -u root -v "$(pwd)":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build