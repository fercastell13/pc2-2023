# Práctica Creativa 2 - 2023

El repositorio de esta práctica se encuentra alojado en el siguiente enlace: https://github.com/fercastell13/pc2-2023<br/><br/>
Autores:<br/>
*Fernando Castell Miñón y Belén Casajús Casado*

## Descripción
En esta práctica se va a desplegar una aplicación (https://github.com/CDPS-ETSIT/practica_creativa2) utilizando diferentes tecnologías.<br/>
Este documento, a la par que de memoria, sirve como guía para el correcto despliegue de la aplicación, con instrucciones detalladas sobre el uso de cada tecnología.

## Despliegue de una aplicación escalable

### 1. Despliegue de la aplicación en máquina virtual pesada (2 puntos)
En primer lugar se va a proceder al despliegue de manera tradicional: se va a desplegar la aplicación en una máquina virtual como un monolito.<br/>
Esto se lleva a cabo con un script de python(*pc2.py*), que consta de tres partes:<br/>
- La primera será la configuración inicial: clonado de la aplicación e instalación de las herramientas necesarias (git, pip y python)
- La segunda, la instalación de dependencias presentes en el archivo **requirementes.txt**
- Por último, se procede a cambiar la varibale de entorno **GRUPO_NUMERO** y a la ejecución de la aplicación en el puerto 9080 con la siguiente orden:
~~~
subprocess.check_call(["python3", "./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", str(puerto)])
~~~

El despliegue de esta aplicación se lleva a cabo en una máquina virtual de Google Cloud Platform. Por ello, a continucación se detallan los pasos a seguir para el correcto funcionamiento:
- Una vez dentro de GCP, creamos una nueva instancia de una máquina virtual con las siguientes especificaciones:
    - Como sistema operativo: Debian GNU/Linux 10
    - Permitir el tráfico HTTP y HTTPS
- A continuación, se abre una terminal y se procede al despliegue de la app de la siguiente manera:
~~~
sudo apt-get update
sudo apt-get -y install git
git clone https://github.com/fercastell13/pc2-2023.git
cd pc2-2023
python3 pc2.py
~~~

- Por último, hace falta crear una regla en el firewall de la máquina virtual. Para ello, se accede a "Detalles de Red" (VPC Network) -> Firewall -> Crear regla de Firewall y se le dan los siguientes valores:
    - Name: port-9080-allow
    - Red: valor por defecto
    - Prioridad: valor por defecto
    - Direction of traffic: Selecciona la dirección del tráfico (Ingress para tráfico entrante).
    - Acción: permitir
    - Targets: selecciona "Todas las instancias en la red
    - Source filter: 0.0.0.0/0
    - Protocolos y puertos: añadir un puerto TCP con valor 9080

Una vez hecho esto, la aplicación estará accesible a través del navegador con la siguiente orden:
~~~
http://<ip-publica>:<puerto>/productpage
~~~

### 2.- Despliegue de una aplicación monolítica usando docker (2 puntos)

La imagen creada con Dockerfile se encuentra disponible en DockerHub a través del siguiente enlace:<br/>
https://hub.docker.com/repository/docker/fernandocastell/product-page

Se crea un archivo Dockerfile, abriendo el puerto 9080, haciendo el clonado de la aplicación, se instalan las dependencias necesarias con el fichero *requirements.txt*.<br/>
Se crea la variable de entorno y se sustituye en el HTML.
Por último, se lanza la aplicación en el puerto 9080 con el siguiente comando:
~~~
CMD ["python3", "./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", "9080"]

~~~

Necesitamos iniciar el servicio de Docker. A través de la terminal sería:
~~~
sudo service docker start
~~~
En Windows:
~~~
Start-Service Docker
~~~

El proceso, por si no era lo suficientemente simple, se ha automatizado con el fichero *auto-docker.sh*, por lo que será suficiente un único paso:

Ejecutar auto-docker.sh:
~~~
./auto-docker.sh
~~~
Alternativamente, en windows:
~~~
.\auto-docker.sh
~~~

Ahora solo será necesario abrir el navegador:
~~~
http://localhost:9080/product-page
~~~

El resultado por pantalla será algo parecido a lo siguiente:<br>

![Imagen del despliegue de Docker](./images/image.png)

### 3.- Segmentación de una aplicación monolítica en microservicios utilizando docker-compose ( 2 puntos)
//TODO

### 4.- Despliegue de una aplicación basada en microservicios utilizando Kubernetes (4 puntos)
//TODO


Hemos añadido un FW para habilitar el tráfico en el puerto 9080. Ahora sale la app correctamente, aunque sin estilo.
La aplicación se encuentra corriendo en http://34.140.34.89:9080/ (no funciona en HTTPS)

