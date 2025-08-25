from flask import render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from app import app, db
from app.forms import NomeForm, ProdutoForm
from app.models import Produto, Usuario

# Aula 1 — Introdução e primeira rota
@app.route("/")
def index():
    return render_template("index.html", title="Página Inicial")

@app.route("/sobre")
def sobre():
    return render_template("about.html", title="Sobre o Projeto")

# Aula 2 — Formulários
'''
@app.route("/form", methods=["GET", "POST"])
def form():
    form = NomeForm()
    mensagem = None
    if form.validate_on_submit():
        nome = form.nome.data
        mensagem = f"Olá, {nome}! Formulário recebido com sucesso."
    return render_template("form.html", title="Formulário", form=form, mensagem=mensagem)
'''

# Aula 7 — Autenticação e Autorização
@app.route("/form", methods=["GET", "POST"])
def form():
    form = NomeForm()
    mensagem = None
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        senha = form.senha.data

        # Verifica se já existe usuário com este email
        existente = Usuario.query.filter_by(email=email).first()
        if existente:
            mensagem = "E-mail já cadastrado."
        else:
            usuario = Usuario(nome=nome, email=email)
            usuario.set_password(senha)
            db.session.add(usuario)
            db.session.commit()
            mensagem = f"Usuário {nome} cadastrado com sucesso!"
    return render_template("form.html", title="Cadastro Usuário", form=form, mensagem=mensagem)


# Aula 3 — API REST
@app.route("/api/dados")
def api_dados():
    dados = [
        {"id": 1, "nome": "Ana Vitória"},
        {"id": 2, "nome": "Anderson Freitas"},
        {"id": 3, "nome": "Felipe Maia"}
    ]
    return jsonify(dados)

# Aula 4 - CRUD com banco de dados
@app.route("/produtos")
def listar_produtos():
    produtos = Produto.query.all()
    return render_template("produtos.html", title="Lista de Produtos", produtos=produtos)

@app.route("/produto/novo", methods=["GET", "POST"])
def novo_produto():
    form = ProdutoForm()
    if form.validate_on_submit():
        produto = Produto(
            nome=form.nome.data,
            preco=form.preco.data,
            estoque=form.estoque.data
        )
        db.session.add(produto)
        db.session.commit()
        flash("Produto cadastrado com sucesso!", "success")
        return redirect(url_for("listar_produtos"))
    return render_template("produto_form.html", title="Novo Produto", form=form)

@app.route("/produto/<int:id>/editar", methods=["GET", "POST"])
def editar_produto(id):
    produto = Produto.query.get_or_404(id)
    form = ProdutoForm(obj=produto)
    if form.validate_on_submit():
        produto.nome = form.nome.data
        produto.preco = form.preco.data
        produto.estoque = form.estoque.data
        db.session.commit()
        flash("Produto atualizado com sucesso!", "success")
        return redirect(url_for("listar_produtos"))
    return render_template("produto_form.html", title="Editar Produto", form=form)

@app.route("/produto/<int:id>/excluir", methods=["POST"])
def excluir_produto(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    flash("Produto excluído com sucesso!", "success")
    return redirect(url_for("listar_produtos"))

# Aula 5 - API com banco de dados
@app.route("/api/produtos", methods=["GET", "POST"])
def api_produtos():
    if request.method == "POST":
        data = request.get_json()
        produto = Produto(
            nome=data['nome'],
            preco=data.get('preco', 0),
            estoque=data.get('estoque', 0)
        )
        db.session.add(produto)
        db.session.commit()
        return jsonify(produto.to_dict()), 201
    
    produtos = Produto.query.all()
    return jsonify([produto.to_dict() for produto in produtos])

@app.route("/api/produtos/<int:id>", methods=["GET", "PUT", "DELETE"])
def api_produto(id):
    produto = Produto.query.get_or_404(id)
    
    if request.method == "PUT":
        data = request.get_json()
        produto.nome = data['nome']
        produto.preco = data.get('preco', produto.preco)
        produto.estoque = data.get('estoque', produto.estoque)
        db.session.commit()
        return jsonify(produto.to_dict())
    
    if request.method == "DELETE":
        db.session.delete(produto)
        db.session.commit()
        return '', 204
    
    return jsonify(produto.to_dict())

# Aula 7 - Nova rota de login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and usuario.check_password(senha):
            login_user(usuario)
            flash("Login realizado com sucesso!", "success")
            return redirect(url_for("index"))
        else:
            flash("Credenciais inválidas", "danger")
    return render_template("login.html", title="Login")

# Aula 7 - Nova rota de logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Você saiu da conta.", "info")
    return redirect(url_for("index"))

# Aula 7 - Rota protegida (exemplo)
@app.route("/perfil")
@login_required
def perfil():
    return render_template("perfil.html", title="Perfil", usuario=current_user)