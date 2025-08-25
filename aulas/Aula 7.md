# Aula 7 – Autenticação e Autorização

## Objetivos da aula
- Entender os conceitos de **autenticação** (identificar usuários) e **autorização** (controlar acesso a recursos).
- Explorar cenários típicos: login com usuários, controle de acesso baseado em papéis (roles), permissão de rotas, etc.

---

## 1. Conceitos principais
- **Autenticação**: verificar a identidade de um usuário (por exemplo, login com username/senha).
- **Autorização**: determinar se o usuário autenticado tem permissão para executar certa ação ou acessar determinado recurso.
- Diferenças e relação entre os dois.

## 2. Fluxo típico de autenticação
1. O usuário envia credenciais.
2. O servidor valida as credenciais (comparando com dados no banco de dados).
3. Em caso de sucesso, o servidor cria uma **sessão** ou emite um **token de acesso**.
4. Em requisições subsequentes, o cliente apresenta essa sessão ou token para provar que está autenticado.

## 3. Implementando autenticação simples com Flask-Login (exemplo)
- Instalar e configurar `Flask-Login`.
- No `app/__init__.py`: configurar o `LoginManager`.
```python
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

# Dentro de def create_app():
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

```

- Criar ou alterar o modelo de Usuário.
```python
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), default='user')

    def set_password(self, senha):
        self.password_hash = generate_password_hash(senha)

    def check_password(self, senha):
        return check_password_hash(self.password_hash, senha)
```

- Rotas:
  - `/login` — apresenta formulário, valida login, chama `login_user`.
  - `/logout` — usa `logout_user`.
- Decoradores:
  - `@login_required` é usado para proteger rotas que exigem usuário autenticado.
```python
from flask_login import login_required, login_user, logout_user, current_user

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/admin')
@login_required
def admin():
    if current_user.role != 'admin':
        abort(403)
    return render_template('admin.html')

```

## 4. Autorização baseada em papéis (dependendo da aplicação de vocês)
- Definir papéis como: “admin”, “usuário comum”, etc.
- Decoradores customizados (ex.: `@roles_required('admin')`).
- No modelo, armazenar atributo `role`, e nas rotas, verificar esse atributo.

## 5. Entendendo Hashs e Senhas
No passo 3, vimos o seguinte código no modelo:
```python
def set_password(self, senha):
        self.password_hash = generate_password_hash(senha)
```
Para entender melhor o que ele faz: 
- O generate_password_hash(senha) → converte a senha digitada em uma sequência longa e irreversível de caracteres, chamada hash.

- Esse hash é o que vai para o banco (senha_hash).

- Hash é unidirecional: você não consegue converter o hash de volta para a senha original.

Exemplo simples em código:
```python
senha = "123456"
hash = generate_password_hash(senha)
print(hash)  
# Saída: algo como "pbkdf2:sha256:260000$8H8r...$1a2b3c..."
```
- generate_password_hash do Flask usa PBKDF2 + SHA256 (ou outra função segura).

- Ele adiciona um salt automaticamente — um valor aleatório que torna cada hash único, mesmo para senhas iguais.

- Isso protege contra ataques de rainbow tables (tabelas pré-computadas de hashes).

- Comparar senhas é seguro porque nunca armazenamos nem comparamos a senha original, apenas o hash.

Mas ainda temos o seguinte código:
```python
def check_password(self, senha):
    return check_password_hash(self.senha_hash, senha)
```
- Quando o usuário tenta logar, você chama check_password.
- Isso compara a senha digitada com o hash armazenado, internamente aplicando o mesmo hash e salt.
- Retorna True se a senha estiver correta, False caso contrário.
- Assim, mesmo que alguém veja o hash no banco, não consegue descobrir a senha real.


## 6. Exercícios
- Criar um fluxo de login/logout com páginas simples (templates e rotas).
- Testar acesso não autorizado e redirecionamentos.

---

> **Para estudar em casa**:
> - [Documentação Flask-Login](https://flask-login.readthedocs.io/)
