import os
import subprocess

# Obtener el nombre del grupo desde la variable de entorno
group_number = os.getenv("GRUPO_NUMERO")

# Verificar que la variable de entorno está definida
if not group_number:
    raise ValueError("La variable de entorno GRUPO_NUMERO no está definida")

# Definir el puerto en el que se ejecutará la aplicación
app_port = 8080

# Función para ejecutar comandos en la terminal
def run_cmd(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if error:
        raise Exception(f"Error al ejecutar el comando '{cmd}': {error.decode()}")
    return output.decode()

# Función para instalar las dependencias de la aplicación
def install_deps():
    run_cmd("pip3 install -r bookinfo/src/productpage/requirements.txt")

# Función para personalizar la aplicación con el nombre del grupo
def personalize_app():
    # Reemplazar el texto en el archivo HTML
    html_file = "bookinfo/src/productpage/productpage.html"
    with open(html_file, "r") as f:
        html_content = f.read()
    html_content = html_content.replace("NOMBRE_GRUPO", group_number)
    with open(html_file, "w") as f:
        f.write(html_content)

# Función para ejecutar la aplicación
def run_app():
    run_cmd(f"python3 bookinfo/src/productpage/productpage_monolith.py {app_port}")

# Ejecutar las funciones en orden
install_deps()
personalize_app()
run_app()