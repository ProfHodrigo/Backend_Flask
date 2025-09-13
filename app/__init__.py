"""
Aula 8 — Configuração mínima para API com JWT.
- Flask app
- SQLAlchemy para persistir usuários
- JWT para autenticar e proteger rotas da API
- python-dotenv para carregar variáveis de ambiente (.env.dev / .env.prod)
"""

import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Carrega variáveis de ambiente antes de ler os valores
env_file = '.env.dev' if os.getenv('FLASK_ENV') != 'production' else '.env.prod'
load_dotenv(env_file)

app = Flask(__name__, template_folder="templates", static_folder="static")

# Segredos (use valores seguros em produção)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'jwt-secret-dev')

# Banco de dados: usa DATABASE_URL se existir; caso contrário, SQLite local
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', f"sqlite:///{os.path.join(basedir, 'app.db')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialização das extensões
jwt = JWTManager(app)
db = SQLAlchemy(app)

# Garanta que os modelos estejam importados antes de criar as tabelas
from app import models  # noqa: E402,F401

# Cria tabelas automaticamente na primeira execução (dispensa migrations nesta aula)
with app.app_context():
    db.create_all()

# Importa rotas por último, para evitar ciclos de import
from app import routes  # noqa: E402,F401
