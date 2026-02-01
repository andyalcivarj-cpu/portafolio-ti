# Usar una imagen oficial de Python
FROM python:3.12-slim

# Instalar dependencias del sistema necesarias para WeasyPrint en Linux
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-cffi \
    python3-brotli \
    libpango-1.0-0 \
    libharfbuzz0b \
    libpangoft2-1.0-0 \
    libpangocairo-1.0-0 \
    && apt-get clean

# Configurar directorio de trabajo
WORKDIR /app

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el proyecto completo
COPY . .

# Recopilar archivos estáticos (CSS, Imágenes base)
RUN python manage.py collectstatic --no-input

# Comando para ejecutar la aplicación
# Usamos 'proyecto.wsgi' porque así lo indica tu archivo wsgi.py
CMD ["gunicorn", "proyecto.wsgi:application", "--bind", "0.0.0.0:8000"]