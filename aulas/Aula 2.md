## Aula 2 — Templates, HTML Dinâmico, Formulários e Métodos HTTP

### Objetivos
- Entender a herança de templates (Jinja2) e passagem de dados do Python para o HTML.
- Criar páginas dinâmicas com listas e includes.
- Trabalhar com formulários (GET vs POST) usando Flask-WTF e validação básica.

---

### Parte 1 — Templates e HTML dinâmico (Jinja2)

#### Conceitos rápidos
- `templates/` contém arquivos HTML com marcações Jinja2 (`{{ ... }}` e `{% ... %}`).
- `base.html` define o layout comum da aplicação (cabeçalho, rodapé, blocos como `content`).
- Páginas herdam de `base.html` e preenchem os blocos.

#### Passo a passo
1. Abra `app/templates/base.html` e localize o bloco `{% block content %}{% endblock %}`.
2. Abra `app/templates/index.html`.
3. Em `app/routes.py`, passe uma lista de itens (ex.: produtos) para a página inicial:
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
4. Em `app/templates/index.html`, itere sobre `produtos`:
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
5. Recarregue `http://localhost:5000`. Você deverá ver a lista gerada dinamicamente.

##### Exercícios (templates)
- Crie `templates/card.html` e use `{% include 'card.html' %}` dentro do loop para renderizar cada item como um cartão.
- Leia um título por query string: `http://localhost:5000/?titulo=Bem-vindo` e exiba `titulo` na página (use `request.args.get('titulo')`).

---

### Parte 2 — Formulários e métodos HTTP (Flask-WTF)

#### Conceitos rápidos
- GET: buscar/ler recursos (parâmetros na URL).
- POST: enviar dados (formulários, criação).
- Flask-WTF integra WTForms ao Flask e cuida de CSRF e validações.

#### O que já existe no projeto
Em `app/forms.py`, a classe `NomeForm` já possui campos:
```python
class NomeForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Enviar")
```
A rota `/form` (em `app/routes.py`) está configurada para cadastrar um usuário (Aula 7) quando não autenticado.
Se o usuário já estiver autenticado, ela redireciona para `index`.

#### Testando no navegador
1. Acesse `http://localhost:5000/form`.
2. Preencha nome, e-mail e senha e envie.
3. Verifique a mensagem de sucesso no template (mensagens `flash`).

##### Exercícios (formulários)
1. Exiba mensagens de validação ao lado de cada campo no `form.html`.
2. Adicione um campo de confirmação de senha e valide se `senha == confirmacao`.
3. Ao cadastrar o usuário, redirecione para `/login` e mostre uma mensagem informando para realizar login.

---

### Erros comuns e dicas
- Esquecer de configurar `SECRET_KEY` (necessário para CSRF). No projeto, um valor padrão de desenvolvimento já está definido.
- Não ativar o ambiente virtual antes de instalar ou rodar.
- Não tratar `get_flashed_messages()` no layout base para exibir alerts.

---

### Recapitulando
- Você herdou layout com `base.html` e renderizou dados dinâmicos no `index.html`.
- Você utilizou Flask-WTF para criar e validar formulários.
- Rota `/form` no projeto atua como cadastro de usuário (quando não autenticado).
