# seed_data.py

from app import app, db
from app.models import Produto, Usuario # Importe seus modelos

# Dados iniciais que você deseja inserir
PRODUTOS_INICIAIS = [
    {'nome': 'Monitor LED 27"', 'preco': 999.99, 'estoque': 15},
    {'nome': 'Teclado Mecânico RGB', 'preco': 249.50, 'estoque': 30},
    {'nome': 'Mouse Gamer Sem Fio', 'preco': 150.00, 'estoque': 45},
]

def seed_database():
    """Insere dados iniciais no banco de dados."""
    with app.app_context():
        print("Iniciando o processo de seed...")

        # 1. Inserir Produtos
        for produto_data in PRODUTOS_INICIAIS:
            # Verifica se o produto já existe para evitar duplicatas
            if not Produto.query.filter_by(nome=produto_data['nome']).first():
                produto = Produto(**produto_data)
                db.session.add(produto)
                print(f"✅ Produto adicionado: {produto_data['nome']}")
            else:
                print(f"⚠️ Produto já existe: {produto_data['nome']}")

        # 2. Commit das mudanças
        try:
            db.session.commit()
            print("✨ Seed de dados concluído com sucesso!")
        except Exception as e:
            db.session.rollback()
            print(f"❌ Erro ao commitar dados: {e}")

if __name__ == '__main__':
    seed_database()