from utils.db import get_connection
from models.atividade import Atividade

class AtividadeDAO:
    @staticmethod
    def criar(filho_id, titulo, descricao=None, status='pendente'):
        conn = get_connection()
        cur = conn.cursor()
        # verify filho exists
        cur.execute("SELECT id FROM filhos WHERE id = ?", (filho_id,))
        if not cur.fetchone():
            return None, "ATI001"
        cur.execute("INSERT INTO atividades (filho_id, titulo, descricao, status) VALUES (?, ?, ?, ?)", (filho_id, titulo, descricao, status))
        conn.commit()
        aid = cur.lastrowid
        return aid, None

    @staticmethod
    def listar_todos():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, filho_id, titulo, descricao, status FROM atividades")
        rows = cur.fetchall()
        return [Atividade(r["id"], r["filho_id"], r["titulo"], r["descricao"], r["status"]) for r in rows]

    @staticmethod
    def listar_por_filho(filho_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, filho_id, titulo, descricao, status FROM atividades WHERE filho_id = ?", (filho_id,))
        rows = cur.fetchall()
        return [Atividade(r["id"], r["filho_id"], r["titulo"], r["descricao"], r["status"]) for r in rows]
