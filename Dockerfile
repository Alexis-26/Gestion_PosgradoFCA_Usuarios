# Usa la imagen base de Python 3.11.
FROM python:3.11-slim

# Instala unzip y curl, que Reflex necesita para descomprimir y descargar dependencias.
RUN apt-get update && apt-get install -y unzip curl

# Establece el directorio de trabajo dentro del contenedor.
WORKDIR /app

# Copia los archivos de requerimientos e instala las dependencias de Python.
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copia el resto de los archivos de tu proyecto al contenedor.
COPY . .

# Expone los puertos que usa tu aplicación.
EXPOSE 3000
EXPOSE 8000

# Comando para ejecutar la aplicación de Reflex en producción.
CMD ["reflex", "run", "--env", "prod"]