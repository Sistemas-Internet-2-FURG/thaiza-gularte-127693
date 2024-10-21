import sqlite3

def criar_banco_de_dados(db_name='db_letter.db'):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Tabela de Usuários
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL
            )
        ''')

        # Tabela de Livros
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                ano_publicacao INTEGER NOT NULL,
                paginas INTEGER NOT NULL
            )
        ''')

        # Tabela de Favoritos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS favoritos (
                usuario_id INTEGER,
                livro_id INTEGER,
                PRIMARY KEY (usuario_id, livro_id),
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
                FOREIGN KEY (livro_id) REFERENCES livros(id)
            )
        ''')

        # Tabela de Comentários
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS comentarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER,
                livro_id INTEGER,
                comentario TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
                FOREIGN KEY (livro_id) REFERENCES livros(id)
            )
        ''')

        conn.commit()
        print("Banco de dados criado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao criar o banco de dados: {e}")
    finally:
        if conn:
            conn.close()

# Chama a função para criar o banco de dados
criar_banco_de_dados()
