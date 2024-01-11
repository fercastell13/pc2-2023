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
# 3 formas distintas de hacerlo
# subprocess.check_call(["pip", "install", "-r", "./practica_creativa2/bookinfo/src/productpage/requirements.txt"])
# subprocess.check_call(["python3", "-m", "pip", "install", "-r", "./practica_creativa2/bookinfo/src/productpage/requirements.txt"])
os.system('python3 -m pip install -r ./practica_creativa2/bookinfo/src/productpage/requirements.txt')

# # Instalación de  librerias que dan problemas de versiones
# os.system('pip install urllib3')
# os.system('pip install flask_bootstrap')
# os.system('pip install jaeger-client')
# os.system('pip install opentracing-instrumentation')

# Declaración de la variable de entorno <GRUPO_NUMERO>
# os.environ.setdefault('GRUPO_NUMERO', '21')
# grupo_numero = os.getenv('GRUPO_NUMERO')

##
os.environ['GRUPO_NUMERO'] = '21'
grupo_numero = os.getenv('GRUPO_NUMERO')


# Modificación del título de la app para que aparezca el valor de la variable de entorno.
# Para el archivo index.html
# with open("./practica_creativa2/bookinfo/src/productpage/templates/index.html", "r") as f:
#     code = f.read()
# code = code.replace("Simple Bookstore App", str(grupo_numero))
# with open("./practica_creativa2/bookinfo/src/productpage/templates/index.html", "w") as f:
#     f.write(code)
# # Para productpage.html
# with open("./practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "r") as f:
#     code = f.read()
# code = code.replace("Simple Bookstore App", str(grupo_numero))
# with open("./practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "w") as f:
#     f.write(code)



# Nueva version
    
# Modificar el título en index.html
index_html_path = "./practica_creativa2/bookinfo/src/productpage/templates/index.html"
with open(index_html_path, "r") as f:
    content = f.read()

# Buscar y reemplazar el texto del título en index.html
old_title = "Simple Bookstore App"
new_title = str(grupo_numero)
content = content.replace(old_title, new_title)

# Guardar los cambios en index.html
with open(index_html_path, "w") as f:
    f.write(content)


# Por último, ejecutar la aplicación especificando el puerto deseado
subprocess.check_call(["python3", "./practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", str(puerto)])
