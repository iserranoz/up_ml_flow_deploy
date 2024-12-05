# Imagen base de Python
FROM python:3.9-slim

# Configurar el directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema (si son necesarias)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copiar el archivo de dependencias
COPY requirements.txt .

# Instalar las dependencias en Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY app /app/app

# Copiar la carpeta de artefactos
COPY artifacts /app/artifacts

# Configurar variable de entorno para credenciales
ENV GOOGLE_APPLICATION_CREDENTIALS='/secrets/credentials'

# Exponer el puerto de la aplicación
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]