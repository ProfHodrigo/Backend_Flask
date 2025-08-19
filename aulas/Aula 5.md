## Aula 5 — CRUD com Banco de Dados

# Objetivo
Implementar todas as operações **CRUD (Create, Read, Update, Delete)** em nossa aplicação Flask com banco de dados, utilizando formulários, templates e também uma API REST.

---

# O que é CRUD?
CRUD é o conjunto das quatro operações fundamentais em qualquer sistema que manipula dados:

- **Create (Criar)** → inserir novos registros  
- **Read (Ler/Listar)** → consultar registros existentes  
- **Update (Atualizar)** → modificar registros  
- **Delete (Excluir)** → remover registros  

No nosso projeto, vamos aplicar isso à entidade **Produto**.

---

# Modelo de Dados
Em `app/models.py`, já temos a classe `Produto` definida:

```python
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float)
    estoque = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'preco': self.preco,
            'estoque': self.estoque
        }
```
Esse modelo será usado em todas as operações de CRUD.

---

# Rotas CRUD

Em `app/routes.py`, temos as seguintes rotas implementadas:

* GET `/produtos` → Lista todos os produtos

* GET `/produto/novo` → Exibe formulário de criação

* POST `/produto/novo` → Processa criação

* GET `/produto/<id>/editar` → Exibe formulário de edição

* POST `/produto/<id>/editar` → Processa edição

* POST `/produto/<id>/excluir` → Exclui o produto

Além disso, também temos uma API REST:

* GET `/api/produtos` → Retorna lista de produtos em JSON

* POST `/api/produtos` → Cria produto via JSON

* GET `/api/produtos/<id>` → Retorna produto específico

* PUT `/api/produtos/<id>` → Atualiza produto via JSON

* DELETE `/api/produtos/<id>` → Exclui produto

---

# Exemplo de Criação de Produto
Em `routes.py`:
```python
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

```
Esse código:
1. Exibe o formulário (GET)
2. Valida os dados enviados (POST)
3. Salva o produto no banco 
4. Redireciona para a lista de produtos

---

# Exercícios

1. Adicione um campo de descrição no modelo Produto. 
   * Atualize o formulário (produto_form.html) para permitir preencher a descrição. 
   * Exiba a descrição na listagem de produtos. 
   * Na API, garanta que a descrição também apareça no JSON retornado.
   

2. Padronize o `routes.py` de modo que o CRUD utilize GET, POST, PUT e DELETE
   * Verifique quais rotas realizam as mesmas operações.
   * Remova as rotas deplicadas.
   * Atualize os arquivos html de acordo.