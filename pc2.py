# CDPS 2023
#  Práctica creativa 2
# Grupo 21
#!/usr/bin/python3


#TODO: probar en GCP
import os
import subprocess

# Puerto del servicio para google cloud
puerto = 8080 #80 #Use a port number above 1024

# Actualización del sistema
os.system('sudo apt-get -y update') # os.system('sudo apt.get -y update')
os.system('sudo apt-get -y upgrade') # os.system('sudo apt.get -y upgrade')


# Instalaciones necesarias: git, python, pip
# Clonado de la practica
os.system('sudo apt-get -y install git python3 python3-pip') # python3.8
os.system('git clone https://github.com/CDPS-ETSIT/practica_creativa2.git')

# Instalación de las dependencias (requirements.txt)
# subprocess.check_call(["pip", "install", "-r", "./practica_creativa2/bookinfo/src/productpage/requirements.txt"])
subprocess.check_call(["python3", "-m", "pip", "install", "-r", "./practica_creativa2/bookinfo/src/productpage/requirements.txt"])
#os.system('python3 -m pip install -r ./practica_creativa2/bookinfo/src/productpage/requirements.txt')




# Instalamos las librerias que dan problemas de versiones
os.system('pip install urllib3')
os.system('pip install flask_bootstrap')
os.system('pip install jaeger-client')
os.system('pip install opentracing-instrumentation')

# Declaración de la variable de entorno <GRUPO_NUMERO>
os.environ.setdefault('GRUPO_NUMERO', '21')
grupo_numero = os.getenv('GRUPO_NUMERO')
# Modificamos el titulo de la app para que aparezca el valor de la variable de entorno.
# Para index.html
with open("./practica_creativa2/bookinfo/src/productpage/templates/index.html", "r") as f:
    code = f.read()
code = code.replace("Simple Bookstore App", str(grupo_numero))
with open("./practica_creativa2/bookinfo/src/productpage/templates/index.html", "w") as f:
    f.write(code)
# Para productpage.html
with open("./practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "r") as f:
    code = f.read()
code = code.replace("Simple Bookstore App", str(grupo_numero))
with open("./practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "w") as f:
    f.write(code)

# Ejecutar la aplicación especificando el puerto deseado
subprocess.check_call(["python3", "./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", str(puerto)])
# os.system('python3 ./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py str(puerto)') # Same as UP
