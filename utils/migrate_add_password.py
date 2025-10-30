import sqlite3
import bcrypt
import os

# Caminho para o banco SQLite (ajuste se o nome for diferente)
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'artistick.db')

def column_exists(conn, table, column):
    cur = conn.execute(f"PRAGMA table_info({table})")
    cols = [r[1] for r in cur.fetchall()]
    return column in cols

def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # 1️⃣ Adicionar coluna 'password' se ainda não existir
    if not column_exists(conn, "usuarios", "password"):
        cur.execute("ALTER TABLE usuarios ADD COLUMN password TEXT")
        conn.commit()
        print("✅ Coluna 'password' adicionada.")
    else:
        print("ℹ️ Coluna 'password' já existe.")

    # 2️⃣ Popular senhas hashadas para usuários que ainda não têm
    cur.execute("SELECT id FROM usuarios WHERE password IS NULL OR trim(password) = ''")
    rows = cur.fetchall()

    print(f"👤 Usuários sem senha: {len(rows)}")
    for (uid,) in [(r['id'],) for r in rows]:
        senha_temp = "SenhaTemporaria123"  # pode mudar
        hashed = bcrypt.hashpw(senha_temp.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        cur.execute("UPDATE usuarios SET password = ? WHERE id = ?", (hashed, uid))

    conn.commit()
    conn.close()
    print("✅ Senhas temporárias adicionadas (hashadas com bcrypt).")

if __name__ == "__main__":
    main()
