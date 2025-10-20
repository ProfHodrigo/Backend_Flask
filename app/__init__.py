from flask import Flask, json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

if not hasattr(json, 'JSONEncoder'):
    from json import JSONEncoder
    json.JSONEncoder = JSONEncoder

app = Flask(__name__, template_folder="templates", static_folder="static")

CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Carrega variáveis de ambiente ANTES de usá-las para configurar
# Usamos o padrão do FLASK_ENV para carregar o arquivo .env correto
env_file = '.env.dev' if os.getenv('FLASK_ENV') != 'production' else '.env.prod'
load_dotenv(env_file)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY", "jwt-secret-dev")
jwt = JWTManager(app)

# ---
## Configuração do Banco de Dados Local (SQLite)
# ---
basedir = os.path.abspath(os.path.dirname(__file__))
# A URL do banco de dados está agora fixa para usar o SQLite local (app.db)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = "login"
# login_manager.login_message = "Você precisa estar logado para acessar esta página."

from app.models import Usuario

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))


app.config['DEBUG'] = os.getenv('DEBUG', 'False') == 'True'
app.config['ENV'] = os.getenv('FLASK_ENV', 'production')

from app import routes, models