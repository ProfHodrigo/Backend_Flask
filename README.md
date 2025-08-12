# Backend_Flask — Curso

Projeto didático para as 3 primeiras aulas de Backend com Framework.

## Aulas
1. Introdução ao Flask, rotas básicas.
2. Templates, HTML dinâmico, Formulários e métodos HTTP.
4. API REST com retorno JSON.

## Requisitos
- Linux (Ubuntu/Debian recomendado)
- Python 3.10
- Git (opcional, para controle de versão)

## Instalação rápida (para iniciar as aulas)
```bash
# 1) clone (ou copie os arquivos já disponibilizados)
git clone https://github.com/ProfHodrigo/Backend_Flask.git
cd Backend_Flask

# 2) crie e ative venv (Python 3.10)
python3.10 -m venv venv
source venv/bin/activate

# 3) instale dependências
pip install --upgrade pip
pip install -r requirements.txt

# 4) rode a aplicação
python run.py
```

Abra no navegador: `http://localhost:5000`

---

# Plano passo-a-passo das aulas

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

---

## Aula 2 — Templates, HTML Dinâmico, Formulários e Métodos HTTP
**Objetivo:** entender templates Jinja2, herança de templates (`base.html`) e como passar variáveis do Python para HTML.

### Conceitos rápidos
- `templates/` contém arquivos HTML com marcações Jinja2 (`{{ ... }}` e `{% ... %}`).
- `base.html` geralmente contém o layout (header/footer) e `block`s para cada página herdar.

### Passo a passo
1. Abra `app/templates/base.html` para ver a estrutura básica e o bloco `{% block content %}{% endblock %}`.
2. Abra `app/templates/index.html`. Atualmente é estático — vamos torná-lo dinâmico.
3. Modifique `app/routes.py` para passar uma lista de itens (ex.: produtos) para a página inicial. Substitua a função `index()` por este exemplo:

```python
@app.route("/")
def index():
    produtos = [
        {"id": 1, "nome": "Caderno"},
        {"id": 2, "nome": "Caneta"},
        {"id": 3, "nome": "Mochila"}
    ]
    return render_template("index.html", title="Página Inicial", produtos=produtos)
```

4. Em `app/templates/index.html`, altere para iterar sobre `produtos`:
```jinja
{% extends "base.html" %}
{% block content %}
<h2>Produtos</h2>
<ul>
  {% for p in produtos %}
    <li>{{ p.id }} — {{ p.nome }}</li>
  {% endfor %}
</ul>
{% endblock %}
```

5. Salve e recarregue `http://localhost:5000`. Deve ver a lista gerada dinamicamente.

### Exercício 1
- Adicione um template `templates/card.html` e use `{% include 'card.html' %}` dentro do loop para renderizar cada item em um cartão.
- Passe um título dinâmico (por query string): `http://localhost:5000/?titulo=Bem-vindo` e exiba `titulo` na página.

### Recapitulando até aqui
- `index.html` mostra dados vindos do Python.
- `base.html` é usado como layout comum e a herança funciona corretamente.

---

## Parte 2 — Formulários e Métodos HTTP 

**Objetivo:** trabalhar com formulários HTML, entender GET vs POST e usar Flask-WTF para validação simples.

### Conceitos rápidos
- GET: usado para buscar/ler recursos; parâmetros ficam na URL.
- POST: usado para enviar dados ao servidor (formulários, criação).
- Flask-WTF integra WTForms ao Flask e facilita validação e proteção CSRF.

### Passo a passo
1. Abra `app/forms.py` — já existe a classe `NomeForm` com um campo `nome`:
```python
class NomeForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    submit = SubmitField("Enviar")
```

2. A rota `@app.route("/form", methods=["GET", "POST"])` em `app/routes.py` já usa `NomeForm()` e chama `form.validate_on_submit()`.
3. Teste no navegador: acesse `http://localhost:5000/form`, preencha o nome e envie — deve aparecer a mensagem de confirmação (renderizada pela variável `mensagem` no template).

4. **Tarefa prática:** adicione um campo `email` ao formulário (`forms.py`) com validador `DataRequired()` e `Email()` (importe `Email` de `wtforms.validators`). Atualize o template `form.html` para incluir o campo novo e exiba ambos após submissão.

Exemplo (adição em `forms.py`):
```python
from wtforms.validators import DataRequired, Email
class NomeForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    submit = SubmitField("Enviar")
```

5. **Exercício 2** ao submeter, redirecione para a página inicial com `redirect(url_for('index'))` e passe uma mensagem flash com `flash("...")`. Veja como usar `get_flashed_messages()` no `base.html` para mostrar mensagens.

### Recapitulando até aqui
- Formulário aparece em `GET /form`.
- Submissão via POST valida os campos; se inválido, mostra erro (ou não aceita o envio).
- Ao enviar corretamente, o template exibe a resposta do servidor.

---

## Aula 3 — API REST no Flask
**Objetivo:** criar endpoints que retornem JSON e entender como testar APIs com `curl` ou no navegador.

### Conceitos rápidos
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

---

## Como entregar as atividades (para alunos)
1. Crie um repositório no GitHub com seu nome: `Backend_Flask_<seunome>`.
2. Faça um commit com os exercícios resolvidos: (`git commit -m "Aula1 - rotas básicas"` etc.).
3. Envie o link do repositório ao instrutor (ou pelo e-mail rodrigo.viana@multiversa.com).

### Comandos úteis
```bash
git init
git add .
git commit -m "Aula1 - rotas e templates"
git remote add origin https://github.com/SEU_USUARIO/NOME_REPO.git
git push -u origin main
```

---

## Dicas e resolução de problemas
- Se `flask_wtf` reclamar de CSRF: confira se `SECRET_KEY` está definido (em `app/__init__.py`).
- Se o Flask não reinicia após alterações: pare o servidor (Ctrl+C) e reinicie `python run.py` ou use `FLASK_DEBUG=1`/auto-reload.
- Erros comuns: esquecer de ativar o venv; instalar dependências no Python errado (confirme `python --version`).

---

