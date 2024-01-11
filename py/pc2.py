# CDPS 2023
#  Práctica creativa 2
# Grupo 21
#!/usr/bin/python3

import os
import subprocess

# Puerto del servicio para google cloud
puerto = 9080 #Use a port number above 1024 -- regla FW

# Actualización del sistema
os.system('sudo apt-get -y update')
os.system('sudo apt-get -y upgrade')

# Instalaciones necesarias: git, python, pip
# Clonado de la practica
os.system('sudo apt-get -y install git python3 python3-pip') # python3.8
os.system('git clone https://github.com/CDPS-ETSIT/practica_creativa2.git')

# Instalación de las dependencias (requirements.txt)
# 3 formas distintas de hacerlo
# subprocess.check_call(["pip", "install", "-r", "./practica_creativa2/bookinfo/src/productpage/requirements.txt"])
# subprocess.check_call(["python3", "-m", "pip", "install", "-r", "./practica_creativa2/bookinfo/src/productpage/requirements.txt"])
os.system('python3 -m pip install -r ./practica_creativa2/bookinfo/src/productpage/requirements.txt')

# Instalar -- no creo que haga falta pero funciona #TODO
os.system('python3 -m pip install Flask-Bootstrap==3.3.7.1')

# Declaración de la variable de entorno <GRUPO_NUMERO>
os.environ['GRUPO_NUMERO'] = '21'
grupo_numero = os.getenv('GRUPO_NUMERO')

# Modificar el título en el index.html y en productpage.html
# VARIABLE DE ENTORNO
ruta_pp = "./practica_creativa2/bookinfo/src/productpage/templates/productpage.html"
ruta_index = "./practica_creativa2/bookinfo/src/productpage/templates/index.html"
with open(ruta_index, "r") as f:
    codigo = f.read()

# Buscar y reemplazar el texto del título en index.html
titulo = "Simple Bookstore App"
nuevo_titulo = str(grupo_numero)
codigo = codigo.replace(titulo, nuevo_titulo)

# Guardar los cambios en index.html
with open(ruta_index, "w") as f:
    f.write(codigo)
# Guardar los cambios en productpage.html
with open(ruta_pp, "w") as f:
    f.write(codigo)

# Por último, ejecutar la aplicación especificando el puerto deseado indicado al principio del documento
subprocess.check_call(["python3", "./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", str(puerto)])