# Backend_Flask — Curso

Projeto didático para as 3 primeiras aulas de Backend com Framework.

## Aulas
1. Introdução ao Flask, rotas básicas.
2. Templates, HTML dinâmico, Formulários e métodos HTTP.
3. API REST com retorno JSON.
4. Persistência de dados e modelagem com SQLAlchemy.
5. CRUD completo com banco de dados.
6. Migrations e deploy para produção.
7. Autenticação e Autorização
8. Geração e Validação de Tokens JWT
9. Passo-a-passo para configuração da aplicação
10. Revisão para a Avaliação

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
