## Aula 1 — Introdução ao Flask
**Objetivo:** entender o que é backend e criar a rota mínima em Flask.

### Conceitos rápidos
- Backend: parte da aplicação que roda no servidor e responde a requisições HTTP (páginas HTML, JSON, etc).
- Flask: microframework Python para criar aplicações web com rotas simples.

### Passo a passo
1. Inicie o servidor: `python run.py`
2. Acesse `http://localhost:5000` — deve abrir a *Página Inicial* (arquivo `app/templates/index.html`).
3. Abra `app/routes.py` e localize a função `index()`:

```python
@app.route("/")
def index():
    return render_template("index.html", title="Página Inicial")
```

4. **Exercício 1** — adicione uma rota `/hello` que retorna texto simples. Copie esse bloco em `app/routes.py`:
```python
@app.route("/hello")
def hello():
    return "Olá, mundo — esta é a rota /hello"
```
Salve o arquivo e atualize a página `http://localhost:5000/hello` — deve aparecer a mensagem de texto.

5. **Exercício 2** crie `/hello/<nome>` que exiba `Olá, <nome>!` usando o parâmetro de rota:
```python
@app.route("/hello/<nome>")
def hello_nome(nome):
    return f"Olá, {nome}!"
```

### Recapitulando: Aula 1
- `GET /` abre a página inicial.
- `GET /hello` retorna texto simples.
- `GET /hello/Rodrigo` retorna `Olá, Rodrigo!`