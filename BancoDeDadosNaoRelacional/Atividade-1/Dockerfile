# Imagem base oficial do Python
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos de dependências
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia código da aplicação
COPY . .

# Expõe a porta da aplicação
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]