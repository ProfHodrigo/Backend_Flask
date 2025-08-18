## Aula 5 — CRUD com banco de dados
**Objetivo:** implementar operações Create, Read, Update, Delete.

### Conceitos
**CRUD:** conjunto de operações básicas para manipulação de dados.
**Flask-WTF:** fornece formulários validados para cadastro/edição.
**Flash messages:** mensagens exibidas após operações (ex.: "Produto cadastrado com sucesso!").

### Rotas implementadas
`GET /produtos` → Lista todos os produtos
`GET /produto/novo` → Formulário de criação
`POST /produto/novo` → Processa criação
`GET /produto/<id>/editar` → Formulário de edição
`POST /produto/<id>/editar` → Processa edição
`POST /produto/<id>/excluir` → Remove produto

### Exemplo de criação de produto
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
    return render_template("produto_form.html", form=form)
```

**Exercícios**
1. Implemente CRUD para o modelo Usuario.
2. Adicione validação customizada no formulário de Produto.
3. Implemente paginação na lista de produtos.
