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
1. O usuário envia credenciais (e.g., username e senha).
2. O servidor valida as credenciais (comparando com dados armazenados, ex.: banco de dados).
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

- Criar ou alterar o modelo de Usuário: métodos `is_authenticated`, `get_id()` etc.
```python
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), default='user')
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

## 5. Exercícios
- Criar fluxo de login/logout com páginas simples (templates e rotas).
- Testar acesso não autorizado e redirecionamentos.

---

> **Para estudar em casa**:
> - [Documentação Flask-Login](https://flask-login.readthedocs.io/)
