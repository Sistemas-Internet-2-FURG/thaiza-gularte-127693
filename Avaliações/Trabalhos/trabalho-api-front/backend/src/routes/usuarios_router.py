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

@usuarios_bp.route('/home', methods=['GET'])
def acessar_home():
    token = None
    if 'Authorization' in request.headers:
        auth_header = request.headers['Authorization']
        token = auth_header.split(" ")[1]  # Extrai o token após 'Bearer '

    if not token:
        return jsonify({'status': 404, 'message': 'Token ausente!'})

    try:
        # Tenta decodificar o token
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return jsonify({'status': 200, 'message': 'Token válido'})
    except jwt.ExpiredSignatureError:
        return jsonify({'status': 404, 'message': 'Token expirado!'})
    except jwt.InvalidTokenError:
        return jsonify({'status': 404, 'message': 'Token inválido!'})
    

@usuarios_bp.route('/login', methods=['POST'])
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


@usuarios_bp.route('/verificar_email', methods=['POST'])
def verificar_email():
    # Obtém o JSON da requisição
    dados = request.get_json()
    if not dados or 'email' not in dados:
        return jsonify({"code": 400, "msg": "Email não fornecido"}), 400

    email = dados.get('email')

    conn = sqlite3.connect('db_letter.db')
    cursor = conn.cursor()

    try:
        # Busca o usuário pelo email
        cursor.execute('''
            SELECT senha FROM usuarios WHERE email = ? 
        ''', (email,))
        usuario = cursor.fetchone()

        # Verifica se encontrou o usuário
        if usuario:
            return jsonify({
                "code": 200,
                "senha": usuario[0],  # `usuario[0]` contém a senha do banco
                "msg": "Usuário encontrado"
            }), 200
        else:
            return jsonify({
                "code": 404,
                "senha": '',
                "msg": "Usuário não encontrado"
            }), 404

    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")
        return jsonify({
            "code": 500,
            "msg": "Erro ao acessar banco de dados"
        }), 500

    finally:
        conn.close()
