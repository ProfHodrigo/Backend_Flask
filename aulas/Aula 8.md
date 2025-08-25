# Aula 8 – Geração e Validação de Tokens JWT

## Objetivos da aula

- Entender o que é um JWT (JSON Web Token) e por que ele é usado.

- Aprender a gerar tokens no servidor quando o usuário faz login.

- Aprender a validar tokens em rotas protegidas.

- Implementar autenticação baseada em token.

## 1. O que é JWT?

- **JWT** = JSON Web Token.

- É um padrão para representar informações seguras entre cliente e servidor.

- **Formato:** `HEADER.PAYLOAD.SIGNATURE`, codificado em base64.

- Exemplo de token:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJ1c2VyX2lkIjoxLCJyb2xlIjoiYWRtaW4ifQ.
x7YxKPZ5rD2D8c3aEdrfF-9n7qv7ShjQ4bM6oIhZkUo
```

--- 

## 2. Fluxo típico com JWT

1. Usuário faz login (envia email + senha).
2. O servidor valida as credenciais.
3. O servidor gera um JWT assinado contendo informações do usuário (id, role).
4. O cliente guarda o token (localStorage ou headers).
5. Em cada requisição à API, o cliente envia o token no header:
```
Authorization: Bearer <TOKEN>
```
6. O servidor valida o token antes de responder.

--- 

## 3. Implementando no Flask

Usaremos a extensão `Flask-JWT-Extended`.

Instalação

Adicionar no `requirements.txt`:
```
Flask-JWT-Extended==4.6.0
```
Configuração no `__init__.py`
``` python
from flask_jwt_extended import JWTManager

app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY", "jwt-secret-dev")
jwt = JWTManager(app)
```

---


## 4. Criando rota de login que gera JWT
``` python
from flask_jwt_extended import create_access_token
from datetime import timedelta

@app.route("/api/login", methods=["POST"])
def api_login():
    data = request.get_json()
    email = data.get("email")
    senha = data.get("senha")

    usuario = Usuario.query.filter_by(email=email).first()
    if usuario and usuario.check_password(senha):
        # Gera token com expiração de 1 hora
        token = create_access_token(
            identity={"id": usuario.id, "nome": usuario.nome, "role": usuario.role},
            expires_delta=timedelta(hours=1)
        )
        return jsonify({"access_token": token}), 200
    
    return jsonify({"erro": "Credenciais inválidas"}), 401
```
---

## 5. Protegendo rotas com JWT
``` python
from flask_jwt_extended import jwt_required, get_jwt_identity

@app.route("/api/perfil", methods=["GET"])
@jwt_required()
def api_perfil():
    identidade = get_jwt_identity()  # dicionário enviado no identity
    return jsonify({
        "mensagem": "Acesso autorizado",
        "usuario": identidade
    })
```

---

## 6. Exercícios

1. Implemente uma rota `/api/admin` que só permita acesso se o role for "admin".

2. Modifique a expiração do token e veja o que acontece quando ele expira.

3. Teste chamadas com e sem `Authorization: Bearer <token>`usando o Postman ou curl.

---

> **Para estudar em casa:**
> 
> - [Documentação Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/en/stable/)
> 
> - [jwt.io](https://www.jwt.io/) - Playground interativo para entender JWT.