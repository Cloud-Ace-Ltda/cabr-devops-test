# Usa uma imagem oficial leve do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia e instala as dependências primeiro (aproveita cache do Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY . .

# BOAS PRÁTICAS: Cria um usuário não-root para rodar a aplicação
RUN useradd -m appuser
USER appuser

# Define a porta padrão
ENV PORT=8080
EXPOSE 8080

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
