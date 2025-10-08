# ===============================
# Dockerfile - Fase 2 (PyGAD + LLM)
# ===============================

# Imagem base: Python 3.11 slim (leve e moderna)
FROM python:3.11-slim

# Evitar prompts interativos
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependências básicas do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Definir diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto para dentro do container
COPY . /app

# Instalar dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copiar arquivos
COPY . /app

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta do Flask
EXPOSE 5000

# Comando para rodar a API Flask
CMD ["python", "app.py"]
