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

4. **Exercício 2:** adicione um campo `email` ao formulário (`forms.py`) com validador `DataRequired()` e `Email()` (importe `Email` de `wtforms.validators`). Atualize o template `form.html` para incluir o campo novo e exiba ambos após submissão.

Exemplo (adição em `forms.py`):
```python
from wtforms.validators import DataRequired, Email
class NomeForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    submit = SubmitField("Enviar")
```

5. **Exercício 3:** ao submeter, redirecione para a página inicial com `redirect(url_for('index'))` e passe uma mensagem flash com `flash("...")`. O `base.html` já está configurado para aceitar `get_flashed_messages()` e mostrar mensagens.

### Recapitulando até aqui
- Formulário aparece em `GET /form`.
- Submissão via POST valida os campos; se inválido, mostra erro (ou não aceita o envio).
- Ao enviar corretamente, o template exibe a resposta do servidor.