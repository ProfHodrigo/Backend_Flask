from flask import Flask, request, jsonify

# Criamos a aplicação Flask
app = Flask(__name__)

# "Banco de dados" simples em memória
# Cada produto será armazenado como {id: {nome: str, quantidade: int}}
estoque = {
    1: {"nome": "Mouse", "quantidade": 10},
    2: {"nome": "Teclado", "quantidade": 5}
}

# ---------------------------
# ROTA GET - Listar todos os produtos
# testar com curl http://127.0.0.1:5000/produtos
# ---------------------------
@app.route("/produtos", methods=["GET"])
def listar_produtos():
    # Retorna o dicionário 'estoque' como JSON
    return jsonify(estoque), 200


# ---------------------------
# ROTA POST - Adicionar um novo produto
# testar com curl -X POST -H "Content-Type: application/json" -d '{"nome": "Monitor", "quantidade": 3}' http://127.0.0.1:5000/produtos
# ---------------------------
@app.route("/produtos", methods=["POST"])
def adicionar_produto():
    # Recebe os dados enviados no corpo da requisição em formato JSON
    novo_produto = request.get_json()

    # Gera um novo ID automaticamente
    novo_id = max(estoque.keys()) + 1 if estoque else 1

    # Adiciona ao "banco de dados"
    estoque[novo_id] = {
        "nome": novo_produto.get("nome"),
        "quantidade": novo_produto.get("quantidade", 0)
    }

    # Retorna o produto criado com status HTTP 201
    return jsonify({novo_id: estoque[novo_id]}), 201


# ---------------------------
# ROTA PUT - Atualizar um produto existente
# testar com curl -X PUT -H "Content-Type: application/json" -d '{"quantidade": 8}' http://127.0.0.1:5000/produtos/1
# ---------------------------
@app.route("/produtos/<int:produto_id>", methods=["PUT"])
def atualizar_produto(produto_id):
    # Se o produto não existir, retorna erro 404
    if produto_id not in estoque:
        return jsonify({"erro": "Produto não encontrado"}), 404

    # Recebe os novos dados
    dados = request.get_json()

    # Atualiza os campos existentes
    estoque[produto_id]["nome"] = dados.get("nome", estoque[produto_id]["nome"])
    estoque[produto_id]["quantidade"] = dados.get("quantidade", estoque[produto_id]["quantidade"])

    return jsonify({produto_id: estoque[produto_id]}), 200


# ---------------------------
# ROTA DELETE - Remover um produto
# testar com curl -X DELETE http://127.0.0.1:5000/produtos/2
# ---------------------------
@app.route("/produtos/<int:produto_id>", methods=["DELETE"])
def deletar_produto(produto_id):
    # Se o produto não existir, retorna erro 404
    if produto_id not in estoque:
        return jsonify({"erro": "Produto não encontrado"}), 404

    # Remove o produto do "banco de dados"
    del estoque[produto_id]
    return jsonify({"mensagem": "Produto removido com sucesso"}), 200


# ---------------------------
# Ponto de entrada da aplicação
# ---------------------------
if __name__ == "__main__":
    # debug=True para recarregar automaticamente ao salvar mudanças
    app.run(debug=True)
