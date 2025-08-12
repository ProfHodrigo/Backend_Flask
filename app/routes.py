from flask import render_template, request, jsonify, flash, redirect, url_for
from app import app
from app.forms import NomeForm

# Aula 1 — Introdução e primeira rota
@app.route("/")
def index():
    produtos = [
        {"id": 1, "nome": "Caderno"},
        {"id": 2, "nome": "Caneta"},
        {"id": 3, "nome": "Mochila"}
    ]
    return render_template("index.html", title="Página Inicial", produtos=produtos)

@app.route("/sobre")
def sobre():
    return render_template("about.html", title="Sobre o Projeto")

# Aula 2 — Formulários
@app.route("/form", methods=["GET", "POST"])
def form():
    form = NomeForm()
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data

        flash(f"Obrigado, {nome}! Seu e-mail {email} foi registrado com sucesso.", "success")

        return redirect(url_for("index"))

    return render_template("form.html", form=form)

# Aula 3 — API REST
@app.route("/api/dados")
def api_dados():
    dados = [
        {"id": 1, "nome": "Ana Vitória"},
        {"id": 2, "nome": "Anderson Freitas"},
        {"id": 3, "nome": "Felipe Maia"}
    ]
    return jsonify(dados)
