# Imagen base (lenguaje python directamente, no es necesario instalar todo el sistema operativo ya que no lo usariamos en este caso, solo necesitamos el interprete de python y las librerias necesarias para correr el proyecto)
FROM python:3

# Directorio de trabajo en el contenedor (lugar donde se instalaran las dependencias, copiaran los archivos y se ejecutara el proyecto)
WORKDIR /opt/

# Actualizar pip (actualizar el manejador de paquetes de python)
RUN pip install --upgrade pip

# Copiar el repositorio de la app a la carpeta interna de la imagen
COPY app .
# Copiar el archivo a la carpeta de la imagen con las variables de entorno de configuracion de Flask
COPY .flaskenv .
# Copiar el archivo a la carpeta de la imagen con las dependencias necesarias para correr el proyecto
COPY requirements.txt .

# Instalar las dependencias necesarias para correr el proyecto desde el archivo requirements.txt en la imagen
RUN pip install -r requirements.txt

# Comando de ejecucion del contenedor con el proyecto
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

