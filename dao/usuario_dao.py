from utils.db import get_connection
from models.usuario import Usuario

class UsuarioDAO:
    @staticmethod
    def criar(nome, email):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM usuarios WHERE email = ?", (email,))
        if cur.fetchone():
            return None, "USR001"
        cur.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
        conn.commit()
        uid = cur.lastrowid
        return uid, None

    @staticmethod
    def listar_todos():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, nome, email FROM usuarios")
        rows = cur.fetchall()
        return [Usuario(r["id"], r["nome"], r["email"]) for r in rows]

    @staticmethod
    def buscar_por_id(id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, nome, email FROM usuarios WHERE id = ?", (id,))
        r = cur.fetchone()
        if not r:
            return None
        return Usuario(r["id"], r["nome"], r["email"])
