import sqlite3
from flask import Blueprint, jsonify, request

comentarios_bp = Blueprint('comentarios', __name__, template_folder='templates')

@comentarios_bp.route('/criar', methods=['POST'])
def criar_comentario():
    usuario_id = request.form['usuario_id']
    livro_id = request.form['livro_id']
    comentario = request.form['comentario']

    # Conectando ao banco de dados e inserindo os dados
    conn = sqlite3.connect('db_letter.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''INSERT INTO comentarios (usuario_id, livro_id, comentario) VALUES (?, ?, ?)''', (usuario_id, livro_id, comentario))
        conn.commit() 
        response = jsonify({'code': 200, 'msg': 'Comentário criado!'})
    
    except sqlite3.Error as e:
        print(f"Erro ao inserir os dados: {e}")
        response = jsonify({'code': 401, 'msg': 'Erro ao comentar'})
    
    finally:
        conn.close()

    return response  # Retornando a resposta ao final da função

@comentarios_bp.route('/buscar', methods=['GET'])
def buscar_comentarios():
    conn = sqlite3.connect('db_letter.db')
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM comentarios')
        comentarios = cursor.fetchall()  # Obter todos os comentários

        # Formatar os dados para retorno
        comentarios_list = [
            {
                'id': com[0],
                'usuario_id': com[1],
                'livro_id': com[2],
                'comentario': com[3]
            } for com in comentarios
        ]

        response = {'code': 200, 'msg': 'Comentários listados', 'dados': comentarios_list}
    except sqlite3.Error as e:
        print('Erro ao buscar comentários no banco:', e)
        response = {'code': 400, 'msg': 'Erro ao buscar comentários', 'dados': 'ERROR'}
    finally:
        conn.close()

    return jsonify(response)  # Retorne a resposta como JSON

@comentarios_bp.route('/buscar/<int:id>', methods=['GET'])
def buscar_comentario_id(id):
    conn = sqlite3.connect('db_letter.db')
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM comentarios WHERE id = ?', (id,))
        comentario = cursor.fetchone()  # Obter o comentário específico

        if comentario:
            response = {'code': 200, 'msg': 'Comentário encontrado', 'dados': comentario}
        else:
            response = {'code': 404, 'msg': 'Comentário não encontrado', 'dados': None}
    except sqlite3.Error as e:
        print('Erro ao buscar comentário no banco:', e)
        response = {'code': 400, 'msg': 'Erro ao buscar comentário', 'dados': 'ERROR'}
    finally:
        conn.close()

    return jsonify(response)  # Retorne a resposta como JSON
