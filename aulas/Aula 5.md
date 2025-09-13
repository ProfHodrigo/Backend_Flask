## Aula 5 — CRUD com Banco de Dados

### Objetivos
- Implementar as operações CRUD (Create, Read, Update, Delete) para a entidade Produto.
- Entender o fluxo via HTML (templates + formulários) e via API (JSON).
- Considerar autenticação: HTML protegido por sessão (Flask-Login) e API protegida por JWT.

---

### Modelo de dados (Produto)
Em `app/models.py`:
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
> Observação: Utilize `to_dict()` nas respostas JSON da API.

---

### Rotas HTML (com sessão)
Em `app/routes.py` (todas com `@login_required`):
- `GET /produtos` → listagem de produtos (renderiza `produtos.html`).
- `GET /produto/novo` → formulário de criação.
- `POST /produto/novo` → cria produto.
- `GET /produto/<int:id>/editar` → formulário de edição.
- `POST /produto/<int:id>/editar` → atualiza produto.
- `POST /produto/<int:id>/excluir` → exclui produto e redireciona.

Exemplo (criação):
```python
@app.route("/produto/novo", methods=["GET", "POST"])
@login_required
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

Fluxo esperado (HTML):
1. Faça login em `/login`.
2. Acesse `/produtos` para listar.
3. Crie/edite/exclua via formulários (feedback via mensagens `flash`).

---

### API REST (com JWT)
Em `app/routes.py` (todas com `@jwt_required()`):
- `GET /api/produtos` → lista produtos em JSON.
- `POST /api/produtos` → cria produto via JSON.
- `GET /api/produtos/<int:id>` → retorna um produto.
- `PUT /api/produtos/<int:id>` → atualiza produto via JSON.
- `DELETE /api/produtos/<int:id>` → exclui produto.

Exemplo (criação via API):
```python
@app.route("/api/produtos", methods=["GET", "POST"])
@jwt_required()
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
    return jsonify([p.to_dict() for p in produtos])
```

Testes rápidos (assumindo `$TOKEN` obtido em `/login`):
- Linux/Mac:
```bash
curl -H "Authorization: Bearer $TOKEN" http://localhost:5000/api/produtos
curl -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
     -d '{"nome":"Caderno","preco":12.5,"estoque":50}' http://localhost:5000/api/produtos
```
- Windows (PowerShell):
```powershell
$TOKEN = "<COLE_AQUI_O_TOKEN>"
Invoke-RestMethod -Uri "http://localhost:5000/api/produtos" -Method GET -Headers @{ Authorization = "Bearer $TOKEN" }
$body = @{ nome = "Caderno"; preco = 12.5; estoque = 50 } | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:5000/api/produtos" -Method POST -Headers @{ Authorization = "Bearer $TOKEN" } -Body $body -ContentType "application/json"
```

---

### Exercícios
1. Adicione um campo `descricao` ao modelo `Produto`.
   - Crie e aplique migration.
   - Atualize `ProdutoForm`, templates e `to_dict()` para incluir `descricao`.
   - Exiba/edite `descricao` na UI e na API.

2. Padronize rotas e métodos HTTP no `routes.py`.
   - Evite rotas duplicadas para a mesma ação.
   - Use `PUT` e `DELETE` na API para atualização/remoção.

3. Validações extras no formulário.
   - Garanta que `preco >= 0` e `estoque >= 0` (já há validadores de exemplo em `forms.py`).

---

### Dicas e observações
- Lembre-se de obter o token JWT via `/login` para testar a API.
- Mensagens `flash` ajudam a dar feedback na UI HTML.
- Use migrations (Flask-Migrate) sempre que alterar modelos.
- Corrija eventuais mensagens/typos (ex.: "duplicadas" em vez de "deplicadas").
