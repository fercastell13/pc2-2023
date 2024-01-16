#Práctica Creativa 2 - 2023

Autores: Fernando Castell Miñón y Belén Casajús Casado


## Despliegue de una aplicación escalable

### 1. Despliegue de la aplicación en máquina virtual pesada (2 puntos)

//DONE

pc2.py: script que despliega la aplicación encontrada en el aiguiente repositorio:
https://github.com/CDPS-ETSIT/practica_creativa2.git


PASOS PARA crear máquina virtual en GCP
$ sudo apt-get update
$ sudo apt-get -y install git
$ git clone https://github.com/fercastell13/pc2-2023.git
$ cd pc2-2023
$ python3 pc2.py



### 2.- Despliegue de una aplicación monolítica usando docker (2 puntos)
//TODO

### 3.- Segmentación de una aplicación monolítica en microservicios utilizando docker-compose ( 2 puntos)
//TODO

### 4.- Despliegue de una aplicación basada en microservicios utilizando Kubernetes (4 puntos)
//TODO


Hemos añadido un FW para habilitar el tráfico en el puerto 9080. Ahora sale la app correctamente, aunque sin estilo.
La aplicación se encuentra corriendo en http://34.140.34.89:9080/ (no funciona en HTTPS)

