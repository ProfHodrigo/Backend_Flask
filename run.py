"""
Aula 8 — ponto de entrada simples.
Execute: python run.py
Por padrão, roda em http://127.0.0.1:5000
"""
from app import app

if __name__ == "__main__":
    # debug pode ser ativado com FLASK_ENV=development e DEBUG=True no .env.dev
    app.run()
