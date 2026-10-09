FROM python:3.11-slim
WORKDIR /app

# Instalamos Flask y Flask-Cors juntos sin usar archivos txt
RUN pip install --no-cache-dir flask flask-cors

COPY main.py .