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