import sqlite3
import requests

def criar_banco_de_dados(db_name='db_letter.db'):
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

        # Tabela de Livros
        cursor.execute('''CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                ano_publicacao INTEGER NOT NULL,
                paginas INTEGER NOT NULL
            )''')

        # Tabela de Favoritos
        cursor.execute('''CREATE TABLE IF NOT EXISTS favoritos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER,
                livro_id INTEGER,
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
                FOREIGN KEY (livro_id) REFERENCES livros(id)
            )''')

        # Tabela de Comentários
        cursor.execute('''CREATE TABLE IF NOT EXISTS comentarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario_id INTEGER,
                livro_id INTEGER,
                comentario TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
                FOREIGN KEY (livro_id) REFERENCES livros(id)
            )''')

        conn.commit()
        print("Banco de dados criado com sucesso!")

        # Verifica se a tabela de livros está vazia
        if verificar_tabela_vazia(conn):
            popular_livros(conn)

    except sqlite3.Error as e:
        print(f"Erro ao criar o banco de dados: {e}")
    finally:
        if conn:
            conn.close()

def verificar_tabela_vazia(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM livros')
    count = cursor.fetchone()[0]  # Pega o primeiro elemento da tupla
    return count == 0  # Retorna True se a tabela estiver vazia

def popular_livros(conn):
    try:
        response = requests.get("https://stephen-king-api.onrender.com/api/books")
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        livros = response.json().get("data", [])  # Extrai o JSON e pega os dados de livros
        
        print("Dados recebidos da API:", livros)  # Adiciona este print para debugar
        
        # Itera sobre os livros e insere no banco de dados
        for livro in livros:
            print("Livro:", livro)  # Debugging para ver o que cada 'livro' contém
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO livros (titulo, ano_publicacao, paginas)
                              VALUES (?, ?, ?)''', (livro['Title'], livro['Year'], livro['Pages']))
        
        conn.commit()  # Salva as alterações no banco
        print("Tabela de livros populada com sucesso!")

    except requests.RequestException as e:
        print(f"Erro ao buscar dados da API: {e}")
    except sqlite3.Error as e:
        print(f"Erro ao inserir dados no banco: {e}")

# Chama a função para criar o banco de dados
criar_banco_de_dados()
