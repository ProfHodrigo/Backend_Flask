from flask import render_template

from app import app

# Aula 1 — Rotas mínimas
@app.route("/")
def index():
    return render_template("index.html", title="Página Inicial")

@app.route("/hello")
def hello():
    return "Olá, mundo — esta é a rota /hello"

@app.route("/hello/<nome>")
def hello_nome(nome):
    return f"Olá, {nome}!"

