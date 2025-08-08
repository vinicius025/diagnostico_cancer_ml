FROM python:3.11-slim

# Diretório de trabalho
WORKDIR /app

# Copia arquivos do projeto
COPY . .

# Atualiza o pip
RUN pip install --upgrade pip

# Instala dependências
RUN pip install -r requirements.txt

# Expondo porta padrão do Jupyter
EXPOSE 8888

# Comando para rodar o Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
