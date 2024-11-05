import sqlite3
from flask import Blueprint, jsonify, render_template, request, redirect, url_for


livros_bp = Blueprint('livros', __name__, template_folder='templates')

@livros_bp.route('/buscar', methods=['GET'])
def buscar_livros():
    conn = sqlite3.connect('db_letter.db')
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM livros')
        livros = cursor.fetchall()  # Obter todos os livros

        # Formatar os dados para retorno
        livros_list = [
            {
                'id': livro[0],
                'titulo': livro[1],
                'ano_publicacao': livro[2],
                'paginas': livro[3]
            } for livro in livros
        ]

        response = {'code': 200, 'msg': 'Livros listados', 'dados': livros_list}
    except sqlite3.Error as e:
        print('Erro ao buscar livros no banco:', e)
        response = {'code': 400, 'msg': 'Erro ao buscar livros', 'dados': 'ERROR'}
    finally:
        conn.close()

    return jsonify(response)  # Retorne a resposta como JSON

@livros_bp.route('/buscar/<int:id>', methods=['GET'])
def buscar_livro_id(id):
    conn = sqlite3.connect('db_letter.db')
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM livros WHERE id = ?', (id,))
        livro = cursor.fetchone()  # Obter o comentário específico

        if livro:
            response = {'code': 200, 'msg': 'livros encontrado', 'dados': livro}
        else:
            response = {'code': 404, 'msg': 'livros não encontrado', 'dados': None}
    except sqlite3.Error as e:
        print('Erro ao buscar livros no banco:', e)
        response = {'code': 400, 'msg': 'Erro ao buscar livros', 'dados': 'ERROR'}
    finally:
        conn.close()

    return jsonify(response)  # Retorne a resposta como JSON


