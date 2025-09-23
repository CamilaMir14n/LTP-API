from utils.db import get_connection
from models.filho import Filho

class FilhoDAO:
    @staticmethod
    def criar(usuario_id, nome, idade):
        conn = get_connection()
        cur = conn.cursor()
        # verify usuario exists
        cur.execute("SELECT id FROM usuarios WHERE id = ?", (usuario_id,))
        if not cur.fetchone():
            return None, "FIL001"
        cur.execute("INSERT INTO filhos (usuario_id, nome, idade) VALUES (?, ?, ?)", (usuario_id, nome, idade))
        conn.commit()
        fid = cur.lastrowid
        return fid, None

    @staticmethod
    def listar_por_usuario(usuario_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, usuario_id, nome, idade FROM filhos WHERE usuario_id = ?", (usuario_id,))
        rows = cur.fetchall()
        return [Filho(r["id"], r["usuario_id"], r["nome"], r["idade"]) for r in rows]

    @staticmethod
    def buscar_por_id(id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, usuario_id, nome, idade FROM filhos WHERE id = ?", (id,))
        r = cur.fetchone()
        if not r:
            return None
        return Filho(r["id"], r["usuario_id"], r["nome"], r["idade"])
