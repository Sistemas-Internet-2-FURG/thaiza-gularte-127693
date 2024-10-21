import sqlite3
from flask import Blueprint, jsonify, render_template, request, redirect, url_for
import requests
livros_bp = Blueprint('livros', __name__, template_folder='templates')

@livros_bp.route('/criar', methods=['POST'])
def adicionar_da_api():
    url = 'https://stephen-king-api.onrender.com/api/books'

    try:
        response = requests.get(url)
        response.raise_for_status()  

        livros = response.json()

        conn = sqlite3.connect('db_letter.db')
        cursor = conn.cursor()

        for livro in livros:

            titulo = livro.get('title')
            ano_publicacao = livro.get('year')
            paginas = livro.get('pages')  

            cursor.execute('''
                INSERT INTO livros (titulo, ano_publicacao, paginas) VALUES (?, ?, ?)
            ''', (titulo, ano_publicacao, paginas))

        # Fazendo commit das alterações
        conn.commit()

        return jsonify({'code': 200, 'msg': 'Livros adicionados com sucesso!'}), 200

    except requests.RequestException as e:
        print(f'Erro ao acessar a API: {e}')
        return jsonify({'code': 500, 'msg': 'Erro ao acessar a API.'}), 500
    except sqlite3.Error as e:
        print(f'Erro ao acessar o banco de dados: {e}')
        return jsonify({'code': 500, 'msg': 'Erro ao acessar o banco de dados.'}), 500
    finally:
        if conn:
            conn.close()

@livros_bp.route('/buscar', methods=['GET'])
def buscar_livros():
    pass

@livros_bp.route('/buscar/id', methods=['GET'])
def buscar_livro_id():
    pass

