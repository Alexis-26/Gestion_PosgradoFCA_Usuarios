# Usa la imagen base de Python 3.11.
FROM python:3.11-slim

# Instala unzip y curl.
RUN apt-get update && apt-get install -y unzip curl

# Establece el directorio de trabajo.
WORKDIR /app

# Copia los archivos de requerimientos.
COPY requirements.txt ./
# Instala las dependencias de Python.
RUN pip install -r requirements.txt

# Copia todo el resto del proyecto.
COPY . .

# Expone los puertos.
EXPOSE 3000
EXPOSE 8000

# Construye el frontend para producción y luego corre el backend.
# El comando `reflex export` genera el frontend en el directorio `.web`.
# El comando `reflex run --no-frontend` inicia el backend y sirve los archivos de `.web`.
CMD ["reflex", "export", "--frontend-only", "--backend-only"]