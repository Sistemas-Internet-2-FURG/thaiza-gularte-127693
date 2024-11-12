import sqlite3
import string
import jwt
import datetime
from flask import Blueprint, jsonify, request, current_app
import random
# Defina a chave secreta (use uma variável de ambiente em produção)
gen = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(gen) for i in range(12))
SECRET_KEY = key

usuarios_bp = Blueprint('usuarios', __name__, template_folder='templates')


@usuarios_bp.route('/home', methods=['POST'])
def acessar_login():
    email = request.form['email']
    senha = request.form['senha']

    conn = sqlite3.connect('db_letter.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            SELECT * FROM usuarios WHERE email = ? AND senha = ?
        ''', (email, senha))
        usuario = cursor.fetchone()
        
        if usuario:
            # Gera o token JWT se o usuário for autenticado
            payload = {
                'id': usuario[0],  # Suponha que o ID do usuário esteja na primeira coluna
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expira em 1 hora
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

            response = jsonify({
                'code': 200, 
                'msg': 'Usuario autenticado', 
                'dados':usuario,
                'token': token
            })
        else:
            response = jsonify({'code': 401, 'msg': 'Email ou senha inválidos'})
    
    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")
        response = jsonify({'code': 500, 'msg': 'Erro ao acessar banco'})
    
    finally:
        conn.close()

    return response

@usuarios_bp.route('/criar', methods=['POST'])
def cadastrar_usuario():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    # Conectando ao banco de dados e inserindo os dados
    conn = sqlite3.connect('db_letter.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            INSERT INTO usuarios (nome, email, senha)
            VALUES (?, ?, ?)
        ''', (nome, email, senha))
        conn.commit() 
        response = jsonify({'code': 200, 'msg': 'Usuario criado'})
    
    except sqlite3.Error as e:
        print(f"Erro ao inserir os dados: {e}")
        response = jsonify({'code': 401, 'msg': 'Erro ao criar usuário'})
    
    finally:
        conn.close()  # Fechando a conexão, mas sem retorno no `finally`

    return response  # Retornando a resposta ao final da função


@usuarios_bp.route('/buscar', methods=['GET'])
def buscar_usuarios():
    conn = sqlite3.connect('db_letter.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            SELECT * FROM usuarios 
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print('Erro ao buscas usuarios no banco.')
    finally:
        conn.close()
        return

@usuarios_bp.route('/buscar/<int:id>', methods=['GET'])
def buscar_usuario_id(id):
    conn = sqlite3.connect('db_letter.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            SELECT * FROM usuarios WHERE id = ?
        ''', (id,))
        conn.commit()
    except sqlite3.Error as e:
        print('Erro ao buscas usuario no banco.')
    finally:
        conn.close()
        return

