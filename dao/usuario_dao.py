
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

    @staticmethod
    def atualizar(id, nome, email):
        conn = get_connection()
        cur = conn.cursor()
        # Verifica se o usuário existe
        cur.execute("SELECT id FROM usuarios WHERE id = ?", (id,))
        if not cur.fetchone():
            return None, "USR404"
        # Verifica se o email já está em uso por outro usuário
        cur.execute("SELECT id FROM usuarios WHERE email = ? AND id != ?", (email, id))
        if cur.fetchone():
            return None, "USR001"
        cur.execute("UPDATE usuarios SET nome = ?, email = ? WHERE id = ?", (nome, email, id))
        conn.commit()
        return UsuarioDAO.buscar_por_id(id), None

    @staticmethod
    def deletar(id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM usuarios WHERE id = ?", (id,))
        if not cur.fetchone():
            return False, "USR404"
        cur.execute("DELETE FROM usuarios WHERE id = ?", (id,))
        conn.commit()
        return True, None
