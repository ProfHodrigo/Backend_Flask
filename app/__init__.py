from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

if not hasattr(json, 'JSONEncoder'):
    from json import JSONEncoder
    json.JSONEncoder = JSONEncoder

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

# Database configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL',
    f"sqlite:///{os.path.join(basedir, 'app.db')}")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Carrega variáveis de ambiente do arquivo apropriado
env_file = '.env.dev' if os.getenv('FLASK_ENV') != 'production' else '.env.prod'
load_dotenv(env_file)

app.config['DEBUG'] = os.getenv('DEBUG', 'False') == 'True'
app.config['ENV'] = os.getenv('FLASK_ENV', 'production')

from app import routes, models