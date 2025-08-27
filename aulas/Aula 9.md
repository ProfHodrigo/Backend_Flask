# Aula 9 – Passo-a-passo para configuração da aplicação


---


## 1. Preparando o ambiente

### 1.1 Criar e ativar ambiente virtual

Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:
``` powershell
python -m venv venv
venv\\Scripts\\activate
```

### 1.2 Instalar dependências
```bash
pip install -r requirements.txt
```

---

## 2. Selecionando o ambiente

Por padrão, a aplicação carrega .env.dev se FLASK_ENV ≠ production.

Se quisermos rodar em produção, precisamos definir a variável FLASK_ENV.

Linux/Mac:
```bash
export FLASK_ENV=production
```
Windows (PowerShell):
```powershell
setx FLASK_ENV "production"
```

Depois de alterar o FLASK_ENV, feche e reabra o terminal para aplicar.

---

## 3. Arquivos .env

### 3.1 .env.dev
```env
FLASK_ENV=development
DEBUG=True
SECRET_KEY=dev-secret-key
JWT_SECRET_KEY=jwt-secret-dev
```

### 3.2 .env.prod
```env
FLASK_ENV=production
DEBUG=False
SECRET_KEY=prod-secret-key
JWT_SECRET_KEY=jwt-secret-prod
DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_banco
```

---

## 4. Configuração do Banco de Dados
O projeto usa Flask-Migrate para versionar o banco.

### 4.1 Ambiente de Desenvolvimento (SQLite)
```bash
flask --app run.py db init     # apenas na primeira vez
flask --app run.py db migrate -m "tabelas iniciais"
flask --app run.py db upgrade
```
Isso criará app/app.db.

### 4.2 Ambiente de Produção (PostgreSQL)
Criar banco no Postgres:
```sql
CREATE DATABASE nome_banco;
```

Executar migrações:
```bash
flask db upgrade
```

As tabelas serão criadas no Postgres informado no .env.prod.

---

# 5. Executando em Desenvolvimento
```bash
flask run
```

Ou:

```bash
python run.py
```

A aplicação estará em:

```cpp
http://127.0.0.1:5000
```

---

## 6. Executando em Produção
### 6.1 Linux/Mac (Gunicorn)
```bash
gunicorn -w 4 -b 0.0.0.0:8000 run:app
```
Acesse:
```arduino
http://0.0.0.0:8000
```

### 6.2 Windows
```bash
flask --app run.py run
```

### 6.3 Windows com Waitress
Edite run.py:
```python
from waitress import serve

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)
```

E rode:
```bash
python run.py
```

---

## 7. Resumindo
Selecionar ambiente:

- Linux/Mac: export FLASK_ENV=production

- Windows: setx FLASK_ENV "production"

- Dev (SQLite):

```arduino
flask --app run.py run
```

- Prod (Postgres + Linux/Mac):
```nginx
gunicorn -w 4 -b 0.0.0.0:8000 run:app
```

- Prod (Windows simplificado):
```arduino
flask --app run.py run
```

---

## 8. Para praticar em casa
- Configure o .env.dev e rode o projeto com SQLite.

- Configure o .env.prod, crie um banco no Postgres e rode flask db upgrade.

- Rode o servidor em produção com Gunicorn (Linux/Mac) ou flask run (Windows).

- Altere o valor de JWT_SECRET_KEY e veja como os tokens deixam de ser válidos.
