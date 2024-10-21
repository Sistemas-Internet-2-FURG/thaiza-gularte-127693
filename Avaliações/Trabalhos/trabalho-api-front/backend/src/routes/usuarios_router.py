import sqlite3
from flask import Blueprint, jsonify, render_template, request, redirect, url_for

usuarios_bp = Blueprint('usuarios', __name__, template_folder='templates')


@usuarios_bp.route('/home', method=['POST'])
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
            return jsonify({'code': 200, 'msg': 'Usuario está cadastrado', 'dados': usuario})
        else:
            return jsonify({'code': 401, 'msg': 'Email ou senha inválidos'})
    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")
        return jsonify({'code': 500, 'msg': 'Erro ao acessar banco'})
    finally:
        conn.close()
        return

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
            VALUES (?, ?, ?, ?)
        ''', (nome, email, senha))
        conn.commit() 
        return jsonify({'code':200, 'msg': 'Usuario criado'})

    except sqlite3.Error as e:
        print(f"Erro ao inserir os dados: {e}")
        return jsonify({'code':401, 'msg': 'Erro ao criar usuário'})
    finally:
        conn.close()
        return

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

