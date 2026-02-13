# 🚀 API Python com Docker

![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Python](https://img.shields.io/badge/Python-3.11-green)
![Flask](https://img.shields.io/badge/Flask-API-black)

---

## 📌 Sobre o Projeto

Este projeto demonstra a containerização de uma aplicação Python utilizando Docker e Docker Compose.

A aplicação é uma API simples desenvolvida com Flask, criada com o objetivo de demonstrar:

- Criação de imagem Docker
- Execução em container
- Orquestração com Docker Compose
- Versionamento no GitHub

---

## 🛠️ Tecnologias Utilizadas

- Python 3.11  
- Flask  
- Docker  
- Docker Compose  

---

## 📂 Estrutura do Projeto

```
.
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Como Executar o Projeto

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2️⃣ Execute com Docker Compose

```bash
docker-compose up --build
```

### 3️⃣ Acesse no navegador

```
http://localhost:5000
```

---

## 🔎 Endpoints Disponíveis

### GET /
```json
{
  "message": "API rodando com Docker 🚀"
}
```

### GET /saude
```json
{
  "status": "ok"
}
```

### GET /soma?a=10&b=5
```json
{
  "resultado": 15
}
```

---

## 🐳 Dockerfile

A imagem é construída a partir da base:

```
python:3.11-slim
```

O container:

- Define diretório `/app`
- Instala dependências
- Copia o código
- Expõe a porta 5000
- Executa `python app.py`

---

## 📦 Docker Compose

O `docker-compose.yml`:

- Constrói a imagem automaticamente
- Mapeia a porta `5000:5000`
- Define nome do container
- Permite reinicialização automática

---

## 📚 Objetivo Acadêmico

Este projeto demonstra conhecimentos em:

- Containerização
- Criação de imagens Docker
- Orquestração de containers
- Estruturação de projeto versionado
- Fundamentos básicos de DevOps

---

## 👨‍💻 Autor

Felipe Mendonça
Inteligência Artificial / Banco de Dados Não Relacional
FATESG / SENAI
2026
