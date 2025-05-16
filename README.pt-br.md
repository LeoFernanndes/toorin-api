# Toorin API

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/LeoFernanndes/toorin-api/blob/develop/README.pt-br.md)

Api para gestão de uma livraria implementada em django rest framework

## Versão do python
3.9.14

## Instruções
1. Clone o repositório
2. Crie um ambiente virtual dentro do repositório clonado
    python3 -m venv venv (cria o ambiente virtual)
    source venv/bin/activate (ativa o ambiente virtual)
3. Execute a instalação das dependências
    pip install -r requirements.txt
4. Execute as migrações
    python manage.py migrate
5. Adicione os dados iniciais ao banco de dados
    python manage.py loaddata users tipoacesso
6. Execute os testes
    python manage.py test
6. Suba o ambiente de desenvolvimento
    python manage.py runserver 0.0.0.0:8000

## Variáveis de ambiente
Crie um arquivo .env dentro do repositório clonado\
    DB_NAME=toorin\
    DB_USER=admin\
    DB_PASSWORD=password\
    DB_HOST=127.0.0.1\
    DB_PORT=5432

## Usuário admin 
username: username\
password: password123