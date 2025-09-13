from flask import Flask

# Aula 1: configuração mínima do Flask (sem banco, sem autenticação)
app = Flask(__name__, template_folder="templates", static_folder="static")

# Importa as rotas da Aula 1
from app import routes
