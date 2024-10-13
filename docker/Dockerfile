# Usa la imagen oficial de Python como base
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos si lo tienes, si no, puedes omitir este paso
COPY requirements.txt ./

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código de la aplicación al contenedor
COPY ../app /app

# Expon el puerto que usará tu aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "src/app.py"]
