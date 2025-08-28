# Usa la imagen base de Python 3.11
FROM python:3.11-slim

# Instala curl (opcional unzip si no lo necesitas)
RUN apt-get update && apt-get install -y curl

# Directorio de trabajo
WORKDIR /app

# Copia los requerimientos e instala dependencias
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el resto del proyecto
COPY . .

# Expone el puerto dinámico que Railway asigna
EXPOSE 8000

# Arranca solo el backend en producción
CMD ["sh", "-c", "reflex run --env prod --backend-only --host 0.0.0.0 --port ${PORT:-8080}"]


