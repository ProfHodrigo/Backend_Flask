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