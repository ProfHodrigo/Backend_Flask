## Aula 3 — API REST no Flask
**Objetivo:** criar endpoints que retornem JSON e entender como testar APIs com `curl` ou no navegador.

### Conceitos
- JSON é o formato de dados mais usado para APIs REST.
- Rotas podem retornar `jsonify(obj)` — o Flask converte para JSON com o content-type adequado.

### Passo a passo
1. A rota já existente `@app.route("/api/dados")` retorna uma lista fixa de objetos:
```python
@app.route("/api/dados")
def api_dados():
    dados = [
        {"id": 1, "nome": "Ana Vitória"},
        {"id": 2, "nome": "Anderson Freitas"},
        {"id": 3, "nome": "Felipe Maia"}
    ]
    return jsonify(dados)
```

2. No terminal, teste com `curl`:
```bash
curl http://localhost:5000/api/dados
```
Deve receber um JSON com o array de objetos.

3. **Exercício 1:** implemente um endpoint `POST /api/dados` que **adiciona** um novo objeto à lista em memória (observe que sem banco de dados os dados **não persistem** entre reinicializações). Exemplo simples a adicionar em `app/routes.py`:

```python
dados = [{"id": 1, "nome": "Ana Vitória"}, {"id": 2, "nome": "Anderson Freitas"}]

@app.route("/api/dados", methods=["GET", "POST"])
def api_dados():
    if request.method == "POST":
        novo = request.get_json()
        novo['id'] = max([d['id'] for d in dados]) + 1 if dados else 1
        dados.append(novo)
        return jsonify(novo), 201
    return jsonify(dados)
```

Teste POST com `curl`:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"nome":"Diego"}' http://localhost:5000/api/dados
```

4. **Exercício 2:** implemente `GET /api/dados/<int:id>` para retornar um único item ou 404 caso não exista; implemente também `DELETE /api/dados/<int:id>` para remover em memória.

### Recapitulando a aula 3
- `GET /api/dados` retorna JSON corretamente.
- `POST /api/dados` aceita JSON e retorna 201 com o item criado (em memória).