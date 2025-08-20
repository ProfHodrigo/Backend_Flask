## Aula 6 — Migrations e Deploy

# Objetivo 
Aprender a versionar o banco de dados e preparar o projeto para produção.

---

### Conceitos
- **Migrations** permitem rastrear mudanças no schema do banco ao longo do tempo.
- **Flask-Migrate** (baseado no Alembic) automatiza a criação e aplicação de migrations.
- **Variáveis de ambiente** permitem configurar diferentes ambientes (dev, teste, produção).

### Passo a passo
1. Adicione um novo campo ao modelo Produto:
```python
data_criacao = db.Column(db.DateTime, default=datetime)
```
> Lembre-se de importar `from datetime import datetime` no modelo.

2. Gere e aplique a migration:
```bash
flask db migrate -m "Add data_criacao to Produto"
flask db upgrade
```

3. Configure o PostgreSQL para produção:
```bash
# No arquivo .env.dev
DATABASE_URL=postgresql://usuario:senha@localhost/nome_banco
```

4. Abaixo segue o comando flask shell para criar um produto:
```bash
p1 = Produto(nome="Produto XYZ", preco=10.0, estoque=100, descricao='Alguma descrição')
db.session.add(p1)
db.session.commit()
```

---

### Exercícios
1. Corrija as rotas e formulários do Usuário.
2. Adicione o campo `data_criacao` no modelo Usuário.

---

# Setando ambientes de Produção e Desenvolvimento

## 1. Estrutura do Projeto

Arquivos a serem alterados:

- `run.py` → ponto de entrada da aplicação
- `__init__.py` → criação do app e configuração
- `requirements.txt` → dependências do projeto
- `.env.dev` / `.env.prod` → variáveis de ambiente para Dev/Prod

---

## 2. Configuração de Variáveis de Ambiente

**.env.dev**
```
SECRET_KEY=dev-secret-key
DATABASE_URL=sqlite:///app.db
FLASK_ENV=development
DEBUG=True
```

**.env.prod**
```
SECRET_KEY=super-secret-key
DATABASE_URL=postgresql://myappuser:minha_senha_segura@localhost/myappdb
FLASK_ENV=production
DEBUG=False
```


No `__init__.py`:

```python
from dotenv import load_dotenv
import os

env_file = '.env.dev' if os.getenv('FLASK_ENV') != 'production' else '.env.prod'
load_dotenv(env_file)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = os.getenv('DEBUG', 'False') == 'True'
app.config['ENV'] = os.getenv('FLASK_ENV', 'production')
```

---

## 3. Banco de Dados PostgreSQL

**Instalar PostgreSQL:**
```
sudo apt install postgresql postgresql-contrib
```

**Criar usuário e banco:**
```
CREATE DATABASE myappdb;
CREATE USER myappuser WITH PASSWORD 'minha_senha';
GRANT ALL PRIVILEGES ON DATABASE myappdb TO myappuser;
```
Lembrem de trocar o myappdb, myappuser e minha_senha para o nome do seu banco de dados, seu usuário e sua senha.

**Instalar driver Python:**
```
pip install psycopg2-binary
```

**Criar migrations e atualizar banco:**
```bash
flask db init       # só na primeira vez
flask db migrate -m "Initial migration"
flask db upgrade
```

## 4. Rodando a Aplicação
**Desenvolvimento:**
```bash
export FLASK_ENV=development
gunicorn -w 4 -b 0.0.0.0:8000 run:app
```

**Produção:**
```bash
export FLASK_ENV=production
gunicorn -w 4 -b 0.0.0.0:8000 run:app
```
-w 4 → Permite 4 requisições simultâneas

-b 0.0.0.0:8000 → Isso abre a porta e host da nossa aplicação

O endereço não será literalmente 0.0.0.0:8000, será o nosso IPv4, que pode ser verificado utilizando o comando ipconfig

# 5. Observações

* Não usar app.run(debug=True) em produção

* Variáveis sensíveis sempre no .env
* SQLite é ok para dev; Para produção sempre precisaremos de algo mais robusto.
* O Gunicorn gerencia múltiplas requisições

### Exercícios
1. Configure um ambiente de produção com PostgreSQL e teste a aplicação.