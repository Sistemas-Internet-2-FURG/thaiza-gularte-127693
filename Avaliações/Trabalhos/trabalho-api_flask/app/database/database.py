import sqlite3

def criar_banco_de_dados(db_name='db_api_flask.db'):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS revendedoras (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_estabelecimento TEXT NOT NULL,
                email TEXT NOT NULL,
                senha TEXT NOT NULL,
                cnpj TEXT NOT NULL
            )
        ''')

        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS veiculos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_revendedora INTEGER,
                nome TEXT NOT NULL,
                marca TEXT NOT NULL,
                modelo TEXT NOT NULL,
                valor TEXT NOT NULL,
                imagem TEXT, 
                FOREIGN KEY (id_revendedora) REFERENCES revendedoras(id)
            )
        ''')#imagem vai ser link por enquanto

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS funcionarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_revendedora INTEGER,
                nome TEXT NOT NULL,
                documento TEXT NOT NULL,
                nivel_de_vendas TEXT,
                FOREIGN KEY (id_revendedora) REFERENCES revendedoras(id)
            )
        ''')

        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao criar o banco de dados: {e}")
    finally:
        if conn:
            conn.close()
