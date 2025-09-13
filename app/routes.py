"""
Rotas necessárias para a Aula 8:
- /            → status simples para verificar se a API está no ar
- /api/registrar (POST) → cria um usuário
- /api/login     (POST) → autentica e retorna um JWT
- /api/perfil    (GET)  → rota protegida por JWT que retorna dados do usuário atual
"""
from datetime import timedelta
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from app import app, db
from app.models import Usuario


@app.route("/")
def healthcheck():
    """Rota simples para verificar se a API está operacional."""
    return jsonify({"status": "ok", "aula": 8}), 200


@app.route("/api/registrar", methods=["POST"])
def registrar():
    """Cria um novo usuário.
    Espera JSON: {"nome": str, "email": str, "senha": str}
    """
    data = request.get_json(silent=True) or {}
    nome = data.get("nome")
    email = data.get("email")
    senha = data.get("senha")

    # Validações básicas
    if not nome or not email or not senha:
        return jsonify({"erro": "Campos obrigatórios: nome, email, senha"}), 400

    if Usuario.query.filter_by(email=email).first():
        return jsonify({"erro": "E-mail já cadastrado"}), 409

    usuario = Usuario(nome=nome, email=email)
    usuario.set_password(senha)
    db.session.add(usuario)
    db.session.commit()

    return jsonify({"msg": "Usuário criado com sucesso", "usuario": usuario.to_dict()}), 201


@app.route("/api/login", methods=["POST"])
def api_login():
    """Autentica o usuário e retorna um token JWT com expiração definida.
    Espera JSON: {"email": str, "senha": str}
    """
    data = request.get_json(silent=True) or {}
    email = data.get("email")
    senha = data.get("senha")

    if not email or not senha:
        return jsonify({"erro": "Informe email e senha"}), 400

    usuario = Usuario.query.filter_by(email=email).first()
    if not usuario or not usuario.check_password(senha):
        return jsonify({"erro": "Credenciais inválidas"}), 401

    # Importante: use o ID inteiro como identidade do token
    access_token = create_access_token(identity=usuario.id, expires_delta=timedelta(minutes=60))
    return jsonify({"access_token": access_token, "usuario": usuario.to_dict()}), 200


@app.route("/api/perfil", methods=["GET"])
@jwt_required()
def api_perfil():
    """Exibe dados do usuário autenticado via JWT."""
    user_id = get_jwt_identity()
    usuario = Usuario.query.get(user_id)

    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    return jsonify(usuario.to_dict()), 200

