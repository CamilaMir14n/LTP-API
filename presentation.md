# Apresentação - Trabalho Bimestral 3
**Grupo:** Artistick  
**Integrantes:** Ayanna, Ana Clara, Camila  
**Disciplina:** Projeto Integrador 2 / Trabalho Bimestral 3

---

## 1. Tema
Aplicativo Artistick — sugestão de atividades e avaliação de inteligências para crianças.

## 2. Entidades escolhidas
- **Usuário (Responsável)**: cadastra conta e gerencia filhos.
- **Filho**: perfil da criança (relacionado a usuário).
- **Atividade**: atividades recomendadas/registradas para filhos.

## 3. Relacionamentos (MER)
- Usuario (1) — (N) Filho
- Filho (1) — (N) Atividade

## 4. Estrutura do Banco
Tabelas: usuarios, filhos, atividades (ver schema em init_db.py)

## 5. Endpoints principais
- POST /usuarios -> cria usuário
- GET /usuarios -> lista
- GET /usuarios/{id} -> busca por id
- POST /filhos -> cria filho (usuario_id obrigatório)
- GET /filhos?usuario={id} -> lista filhos do usuário
- POST /atividades -> cria atividade (filho_id obrigatório)
- GET /atividades?filho={id} -> lista atividades do filho

## 6. Exemplos de testes (Insomnia)
- Criar usuário
- Criar filho com usuario_id inválido (esperado: erro FIL001)
- Criar atividade com filho inválido (esperado: erro ATI001)

## 7. Conclusão
Implementamos a API com persistência real (SQLite3), arquitetura em camadas e tratamento básico de erros. O próximo passo seria autenticação, upload de mídia e comentários nas atividades.
