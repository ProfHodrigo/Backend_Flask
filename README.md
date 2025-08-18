# Backend_Flask — Curso

Projeto didático para as 3 primeiras aulas de Backend com Framework.

## Aulas
1. Introdução ao Flask, rotas básicas.
2. Templates, HTML dinâmico, Formulários e métodos HTTP.
3. API REST com retorno JSON.
4. Persistência de dados e modelagem com SQLAlchemy.
5. CRUD completo com banco de dados.
6. Migrations e deploy para produção.

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

## Dicas e resolução de problemas
- Se `flask_wtf` reclamar de CSRF: confira se `SECRET_KEY` está definido (em `app/__init__.py`).
- Se o Flask não reinicia após alterações: pare o servidor (Ctrl+C) e reinicie `python run.py` ou use `FLASK_DEBUG=1`/auto-reload.
- Erros comuns: esquecer de ativar o venv; instalar dependências no Python errado (confirme `python --version`).

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

---

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

---

## Aula 4 — Ambientes Virtuais e Persistência de dados com modelagem

# Ambiente Virtual com Python (`venv`)

## O que é o `venv`

O `venv` (ou **virtual environment**) é uma ferramenta do Python que permite criar **ambientes isolados** para projetos. Cada ambiente virtual tem sua própria instalação de Python e suas próprias bibliotecas, separadas das que estão instaladas globalmente no sistema.

---

## Para que ele serve

1. **Isolamento de dependências**  
   Diferentes projetos podem precisar de **versões diferentes da mesma biblioteca**.  
   Exemplo:  
   - Projeto A precisa de `Flask==2.2.5`  
   - Projeto B precisa de `Flask==2.3.7`  
   Com `venv`, cada projeto tem sua própria versão isolada.

2. **Evitar poluição do sistema**  
   Todas as bibliotecas instaladas vão para o Python global sem `venv`, o que pode gerar conflitos e deixar o sistema desorganizado.

3. **Facilidade para reproduzir ambientes**  
   Com `venv`, você pode gerar um arquivo `requirements.txt` com todas as dependências do projeto.  
   Outros desenvolvedores podem criar o mesmo ambiente virtual e instalar exatamente as mesmas bibliotecas.

4. **Testes de versões**  
   Permite testar seu código com diferentes versões de bibliotecas sem afetar outros projetos ou o Python global.

---

## Como usar

### 1. Criar um ambiente virtual
```bash
python -m venv venv
```

Aqui, venv é o nome da pasta onde o ambiente será criado.

### 2. Ativar o ambiente virtual
```bash
.\venv\Scripts\activate # Windows
source venv/bin/activate # Linux
```

### 3. Instalar dependências dentro do ambiente
```bash
pip install -r requirements.txt
```
Essas instalações não afetam o Python global.

### 4. Desativar o ambiente
```bash
deactivate
```

# Persistência de Dados com Modelagem

**Objetivo:** entender modelos de dados e integração com SQLAlchemy.

### Conceitos
- ORM (Object-Relational Mapping) mapeia objetos Python para tabelas no banco.
- SQLAlchemy é o ORM mais popular para Python.
- Modelos definem a estrutura dos dados (classes que herdam de `db.Model`).

### Passo a Passo
1. Examine `app/models.py` para ver as classes `Produto` e `Usuario`.
```python
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float)
    estoque = db.Column(db.Integer, default=0)
```

2. Ativar o ambiente virtual
No terminal, dentro da pasta do projeto:
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows (PowerShell ou CMD)

pip list # Verifiquem que deve estar vazio
pip install -r requirements.txt
```

3. Crie e aplique as migrations:
```python
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```
Isso cria o arquivo `app.db` (SQLite por padrão).

4. Teste no shell do Flask:
```bash
flask shell
from app import db
from app.models import Produto
p = Produto(nome="Notebook", preco=4500.99, estoque=10)
db.session.add(p)
db.session.commit()
Produto.query.all()
```

**Exercícios**
1. Ative o ambiente virtual
2. Crie o arquivo `app.db`
3. Abra o shell interativo do Flask
```python
flask shell # vai ficar com o seguinte símbolo >>>
```
Esse shell já importa automaticamente app e db.
Dentro dele, importe os modelos:
```python
from app.models import Usuario, Produto
```

4. Criar objetos Usuario
Crie e salve usuários no banco:
```python
u1 = Usuario(nome="Maria Silva", email="maria@example.com")
u2 = Usuario(nome="João Souza", email="joao@example.com")

db.session.add(u1)
db.session.add(u2)
db.session.commit()
```

Confirme que foram salvos:
```python
Usuario.query.all()
```

5. Listar produtos e filtrar por preço
Crie alguns produtos:
```python
p1 = Produto(nome="Notebook", preco=4500.99, estoque=10)
p2 = Produto(nome="Caneta", preco=2.50, estoque=100)
p3 = Produto(nome="Celular", preco=2500.00, estoque=20)

db.session.add_all([p1, p2, p3])
db.session.commit()
```

Listar todos:
```python
Produto.query.all()
```

Filtrar apenas produtos com preço maior que 1000:
```python
Produto.query.filter(Produto.preco > 1000).all()
```

6. Excluir um produto
Pegue um produto pelo ID:
```python
p = Produto.query.get(1)   # exemplo: produto com ID=1
```

Exclua e confirme:
```python
db.session.delete(p)
db.session.commit()

Produto.query.all()
```

7. Crie uma lista com vários produtos e depois liste os mesmos com o seguinte comando:
```python
[nome.nome for nome in Produto.query.all()]
```

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

## Aula 6 — Migrations e Deploy
**Objetivo:** entender versionamento de banco e preparar para produção.

### Conceitos
Migrations rastreiam mudanças no schema do banco.
Flask-Migrate (baseado no Alembic) gerencia migrations.
Variáveis de ambiente configuram diferentes ambientes (dev, prod).

### Passo a passo
1. Modifique o modelo Produto adicionando um novo campo:
```python
descricao = db.Column(db.Text)
```

2. Gere e aplique a migration:
```python
flask db migrate -m "Add descricao to Produto"
flask db upgrade
```

3. Configure PostgreSQL para produção:
```python
# No .env
DATABASE_URL=postgresql://usuario:senha@localhost/nome_banco
```

**Exercícios**
1. Adicione um campo data_criacao aos modelos.
2. Implemente seeds para dados iniciais.
3. Configure um ambiente de produção com PostgreSQL.