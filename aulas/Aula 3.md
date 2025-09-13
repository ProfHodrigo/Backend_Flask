## Aula 3 — API REST no Flask

### Objetivos
- Criar endpoints que retornam JSON.
- Entender autenticação por token (JWT) aplicada a endpoints.
- Testar APIs com `curl` (Linux/Mac) e PowerShell (Windows).

---

### Conceitos
- JSON é o formato de dados mais usado em APIs REST.
- Use `return jsonify(obj)` para que o Flask retorne `Content-Type: application/json` corretamente.
- No projeto, rotas de API sensíveis estão protegidas com JWT via `@jwt_required()`.

---

### Endpoint existente: GET /api/dados (protegido por JWT)
Em `app/routes.py`, temos:
```python
@app.route("/api/dados")
@jwt_required()
def api_dados():
    dados = [
        {"id": 1, "nome": "Ana Vitória"},
        {"id": 2, "nome": "Anderson Freitas"},
        {"id": 3, "nome": "Felipe Maia"}
    ]
    return jsonify(dados)
```
Para acessar, você precisa obter um token JWT (veja abaixo) e enviar no cabeçalho `Authorization: Bearer <TOKEN>`.

---

### Obtendo um token JWT neste projeto
- A rota HTML `/login` autentica o usuário via formulário.
- Ao logar com sucesso, um token JWT curto (≈15 min) é gerado e exibido via `flash`.
- Copie esse token para testar as rotas da API.

---

### Testando com curl (Linux/Mac)
```bash
TOKEN="<COLE_AQUI_O_TOKEN>"
curl -H "Authorization: Bearer $TOKEN" http://localhost:5000/api/dados
```

### Testando com PowerShell (Windows)
```powershell
$TOKEN = "<COLE_AQUI_O_TOKEN>"
Invoke-RestMethod -Uri "http://localhost:5000/api/dados" -Method GET -Headers @{ Authorization = "Bearer $TOKEN" }
```
Se o token estiver ausente ou inválido, a API responderá com erro 401/422.

---

### Exercício 1 — `POST /api/dados` (em memória)
Implemente um endpoint que recebe JSON e adiciona um item a uma lista em memória (não persiste em disco). Exemplo base:
```python
from flask import request, jsonify

dados = [{"id": 1, "nome": "Ana"}]

@app.route("/api/dados", methods=["GET", "POST"])
@jwt_required()
def api_dados_memoria():
    if request.method == "POST":
        novo = request.get_json()
        novo['id'] = max([d['id'] for d in dados]) + 1 if dados else 1
        dados.append(novo)
        return jsonify(novo), 201
    return jsonify(dados)
```
Teste (Linux/Mac):
```bash
curl -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
     -d '{"nome":"Diego"}' http://localhost:5000/api/dados
```
Teste (Windows PowerShell):
```powershell
$body = @{ nome = "Diego" } | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:5000/api/dados" -Method POST -Headers @{ Authorization = "Bearer $TOKEN" } -Body $body -ContentType "application/json"
```

### Exercício 2 — Itens por ID e remoção
- `GET /api/dados/<int:id>` → retorna um item ou 404.
- `DELETE /api/dados/<int:id>` → remove o item da lista (em memória).

---

### Recapitulando
- Endpoints JSON usam `jsonify` e, neste projeto, são protegidos com JWT.
- Você aprendeu a obter o token via `/login` e testou com `Authorization: Bearer <TOKEN>`.
- Implementou criação, busca e remoção de itens em memória como exercício.
