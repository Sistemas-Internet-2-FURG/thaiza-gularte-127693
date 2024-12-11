import sqlite3

def criar_banco_de_dados(db_name='db_login.db'):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Tabela de Usuários
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL
            )''')

        conn.commit()
        print("Banco de dados criado com sucesso!")

    except sqlite3.Error as e:
        print(f"Erro ao criar o banco de dados: {e}")
    finally:
        if conn:
            conn.close()
