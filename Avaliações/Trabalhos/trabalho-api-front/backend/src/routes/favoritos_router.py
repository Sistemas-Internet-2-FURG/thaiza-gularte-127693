import sqlite3
from flask import Blueprint, jsonify, render_template, request, redirect, url_for


favoritos_bp = Blueprint('favoritos', __name__, template_folder='templates')

@favoritos_bp.route('/criar', methods=['POST'])
def adicionar_favorito():
    usuario_id = request.form['usuario_id']  # Corrigido para "usuario_id"
    livro_id = request.form['livro_id']  # Corrigido para "livro_id"

    # Conectando ao banco de dados e inserindo os dados
    conn = sqlite3.connect('db_letter.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''INSERT INTO favoritos (usuario_id, livro_id) VALUES (?, ?)''', (usuario_id, livro_id))
        conn.commit() 
        response = jsonify({'code': 200, 'msg': 'Favorito adicionado!'})
    
    except sqlite3.Error as e:
        print(f"Erro ao inserir os dados: {e}")
        response = jsonify({'code': 401, 'msg': 'Erro ao favoritar'})
    
    finally:
        conn.close()

    return response

@favoritos_bp.route('/buscar', methods=['GET'])
def buscar_favoritos():
    conn = sqlite3.connect('db_letter.db')
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM favoritos')
        favoritos = cursor.fetchall() 
        
        # Formatar os dados para retorno
        favoritos_list = [
            {
                'usuario_id': fav[0],
                'livro_id': fav[1],
            } for fav in favoritos
        ]

        response = {'code': 200, 'msg': 'favoritos listados', 'dados': favoritos_list}
    except sqlite3.Error as e:
        print('Erro ao buscar favoritos no banco:', e)
        response = {'code': 400, 'msg': 'Erro ao buscar favoritos', 'dados': 'ERROR'}
    finally:
        conn.close()

    return jsonify(response)  # Retorne a resposta como JSON

@favoritos_bp.route('/buscar/<int:id>', methods=['GET'])
def buscar_favorito_id(id):
    conn = sqlite3.connect('db_letter.db')
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM favoritos WHERE id = ?', (id,))
        favorito = cursor.fetchone()  # Obter o favorito específico

        if favorito:
            response = {'code': 200, 'msg': 'Favorito encontrado', 'dados': favorito}
        else:
            response = {'code': 404, 'msg': 'Favorito não encontrado', 'dados': None}
    except sqlite3.Error as e:
        print('Erro ao buscar favorito no banco:', e)
        response = {'code': 400, 'msg': 'Erro ao buscar favorito', 'dados': 'ERROR'}
    finally:
        conn.close()

    return jsonify(response)  # Retorne a resposta como JSON

