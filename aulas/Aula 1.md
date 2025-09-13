## Aula 1 — Introdução ao Flask

### Objetivos
- Entender o papel do backend e do framework Flask.
- Executar a aplicação localmente.
- Criar rotas simples (texto e com parâmetro de URL).

---

### Pré-requisitos rápidos
- Python instalado (verifique com `python --version`).
- Dependências do projeto instaladas (`pip install -r requirements.txt`).
- Ambiente virtual ativado (recomendado).

---

### Executando o projeto
- Windows (PowerShell):
  1) Ativar venv: `./venv/Scripts/activate` (ou `./.venv/Scripts/Activate.ps1` se você criou `.venv`)
  2) Rodar o servidor: `python run.py`

- Linux/Mac:
  1) `source venv/bin/activate`
  2) `python run.py`

A aplicação ficará acessível em `http://localhost:5000`.

> Observação: Se a sua aplicação já estiver com autenticação (Aula 7 aplicada), ao acessar `/` você pode ser redirecionado para `/login`. Faça login primeiro para visualizar a página inicial.

---

### Arquivos envolvidos
- `run.py`: ponto de entrada (inicia o servidor Flask).
- `app/routes.py`: define as rotas.
- `app/templates/`: páginas HTML (templates Jinja2), como `index.html`.

Exemplo de rota básica (em `app/routes.py`):
```python
@app.route("/")
def index():
    return render_template("index.html", title="Página Inicial")
```

---

### Criando suas primeiras rotas
1) Rota que retorna texto simples:
```python
@app.route("/hello")
def hello():
    return "Olá, mundo — esta é a rota /hello"
```
Acesse `http://localhost:5000/hello` e confira a resposta.

2) Rota com parâmetro de URL:
```python
@app.route("/hello/<nome>")
def hello_nome(nome):
    return f"Olá, {nome}!"
```
Teste com `http://localhost:5000/hello/Rodrigo`.

---

### Exercícios
1. Crie uma rota `/saudacao/<nome>/<int:idade>` que retorne uma frase personalizada usando dois parâmetros.
2. Crie uma rota `/status` que retorne JSON com uma chave `ok: true` usando `from flask import jsonify`.
3. Ajuste a rota `/` para enviar uma variável dinâmica ao template (ex.: um título ou uma lista) e exibi-la no `index.html`.

---

### Verificação rápida (checklist)
- Consegue iniciar o servidor sem erros?
- As rotas `/hello` e `/hello/<nome>` respondem corretamente?
- Consegue ver a página inicial (após login, se aplicável)?

---

### Recapitulando
- `GET /` renderiza um template.
- `GET /hello` retorna texto.
- `GET /hello/<nome>` usa parâmetro de rota para personalizar a resposta.
