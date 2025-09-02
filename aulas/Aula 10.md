# Aula 10 – Revisão para Prova

## 1. Backend em aplicações web
| Conceito       | Explicação |
|----------------|------------|
| Onde roda?     | No servidor |
| Função         | Processar requisições e devolver respostas (HTML, JSON, etc.) |
| Diferença do Frontend | Frontend roda no navegador e cuida da interface |

---

## 2. Flask
| Característica  | Explicação |
|-----------------|------------|
| Tipo            | Microframework em Python |
| Vantagem        | Leve, simples, flexível |
| Uso             | Criar rotas e aplicações web rápidas |

---

## 3. Templates Flask (Jinja2)
**Sintaxe principal:**
- `{{ variavel }}` → exibe valores.
- `{% for ... %}{% endfor %}` → loops.
- `{% if ... %}{% endif %}` → condicionais.

**Objetivo:** Separar lógica (Python) da apresentação (HTML).

---

## 4. Arquivo base.html
- Define layout principal (cabeçalho, rodapé, menu).
- Outras páginas podem **herdar** esse layout.
- Facilita reaproveitamento e consistência do design.

---

## 5. Formato em APIs REST
| Formato | Características |
|---------|----------------|
| XML     | Verboso, difícil de ler |
| JSON    | Simples, leve, compatível → **mais usado** |

---

## 6. Ambientes Virtuais (venv)
| Conceito | Explicação |
|----------|------------|
| O que é  | Espaço isolado para projetos Python |
| Para que serve | Evitar conflitos de dependências |
| Benefício | Cada projeto com suas próprias bibliotecas |

---

## 7. CRUD
| Letra | Operação | Exemplo |
|-------|-----------|---------|
| C     | Create    | Adicionar novo usuário |
| R     | Read      | Listar usuários |
| U     | Update    | Alterar senha de um usuário |
| D     | Delete    | Remover usuário |

---

## 8. Migrations (Flask)
- Controlam e versionam mudanças no banco de dados.
- Permitem criar histórico de alterações.
- Exemplos de mudanças: adicionar coluna, criar tabela, modificar tipo de dado.

---

## 9. Autenticação vs Autorização
| Conceito      | Explicação | Exemplo |
|---------------|------------|---------|
| Autenticação  | Verificar identidade do usuário | Login com senha |
| Autorização   | Definir o que o usuário pode acessar | Permissão de admin |

---

## 10. JWT (JSON Web Token)
**Estrutura:**  
1. Cabeçalho (algoritmo e tipo)  
2. Payload (informações do usuário)  
3. Assinatura (garante integridade)  

**Usos principais:**
- Autenticação em APIs.
- Troca segura de informações entre cliente e servidor.
