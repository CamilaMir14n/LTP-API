from utils.db import get_connection
from models.atividade import Atividade

class AtividadeDAO:

    @staticmethod
    def buscar_por_id(id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, filho_id, titulo, descricao, status FROM atividades WHERE id = ?", (id,))
        r = cur.fetchone()
        if not r:
            return None
        return Atividade(r["id"], r["filho_id"], r["titulo"], r["descricao"], r["status"])

    @staticmethod
    def atualizar(id, filho_id, titulo, descricao, status):
        conn = get_connection()
        cur = conn.cursor()
        # Verifica se a atividade existe
        cur.execute("SELECT id FROM atividades WHERE id = ?", (id,))
        if not cur.fetchone():
            return None, "ATI404"
        # Verifica se o filho existe
        cur.execute("SELECT id FROM filhos WHERE id = ?", (filho_id,))
        if not cur.fetchone():
            return None, "ATI001"
        cur.execute("UPDATE atividades SET filho_id = ?, titulo = ?, descricao = ?, status = ? WHERE id = ?", (filho_id, titulo, descricao, status, id))
        conn.commit()
        return AtividadeDAO.buscar_por_id(id), None

    @staticmethod
    def deletar(id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM atividades WHERE id = ?", (id,))
        if not cur.fetchone():
            return False, "ATI404"
        cur.execute("DELETE FROM atividades WHERE id = ?", (id,))
        conn.commit()
        return True, None
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
