from flask import render_template, request, jsonify
from app import app
from app.forms import NomeForm

# Aula 1 — Introdução e primeira rota
@app.route("/")
def index():
    return render_template("index.html", title="Página Inicial")

@app.route("/sobre")
def sobre():
    return render_template("about.html", title="Sobre o Projeto")

# Aula 2 — Formulários
@app.route("/form", methods=["GET", "POST"])
def form():
    form = NomeForm()
    mensagem = None
    if form.validate_on_submit():
        nome = form.nome.data
        mensagem = f"Olá, {nome}! Formulário recebido com sucesso."
    return render_template("form.html", title="Formulário", form=form, mensagem=mensagem)

# Aula 3 — API REST
@app.route("/api/dados")
def api_dados():
    dados = [
        {"id": 1, "nome": "Ana Vitória"},
        {"id": 2, "nome": "Anderson Freitas"},
        {"id": 3, "nome": "Felipe Maia"}
    ]
    return jsonify(dados)
