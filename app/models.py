"""
Modelos necessários para a Aula 8 (apenas Usuario).
"""
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class Usuario(db.Model):
    """Modelo simples de usuário para autenticação JWT."""
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, senha: str) -> None:
        """Gera o hash da senha e armazena em senha_hash."""
        self.senha_hash = generate_password_hash(senha)

    def check_password(self, senha: str) -> bool:
        """Valida a senha informada comparando com o hash armazenado."""
        return check_password_hash(self.senha_hash, senha)

    def to_dict(self) -> dict:
        """Representação segura para respostas JSON (não expõe hash)."""
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
        }
