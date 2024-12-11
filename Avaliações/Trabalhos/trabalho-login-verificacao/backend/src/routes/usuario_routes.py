import sqlite3
from flask import Blueprint, jsonify, request, render_template

# Define o Blueprint
usuarios_bp = Blueprint('usuarios', __name__, template_folder='templates')

# Rota de login
@usuarios_bp.route('/login', methods=['GET', 'POST'])
def acessar_login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        try:
            conn = sqlite3.connect('db_login.db')
            cursor = conn.cursor()

            # Verifica se o usuário existe no banco
            cursor.execute("SELECT senha FROM usuarios WHERE email = ?", (email,))
            resultado = cursor.fetchone()

            if resultado:
                senha_cadastrada = resultado[0]
                if senha == senha_cadastrada:
                    return jsonify({"mensagem": "Login bem-sucedido!"}), 200
                else:
                    return jsonify({"mensagem": "Senha incorreta!"}), 401
            else:
                return jsonify({"mensagem": "Usuário não encontrado!"}), 404

        except sqlite3.Error as e:
            return jsonify({"erro": f"Erro ao acessar o banco de dados: {e}"}), 500
        finally:
            if conn:
                conn.close()

    # Para a rota GET, renderizamos o template de login
    return render_template('login.html')

# Rota para cadastrar usuários
@usuarios_bp.route('/criar', methods=['GET', 'POST'])
def cadastrar_usuario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        try:
            conn = sqlite3.connect('db_login.db')
            cursor = conn.cursor()

            # Insere o novo usuário no banco
            cursor.execute(
                "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                (nome, email, senha)
            )
            conn.commit()
            return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 201

        except sqlite3.IntegrityError:
            return jsonify({"mensagem": "Email já cadastrado!"}), 400
        except sqlite3.Error as e:
            return jsonify({"erro": f"Erro ao cadastrar usuário: {e}"}), 500
        finally:
            if conn:
                conn.close()

    # Para a rota GET, renderizamos o template de cadastro
    return render_template('cadastrar.html')

@usuarios_bp.route('/validate_password', methods=['POST'])
def validate_password():
    data = request.get_json()
    email = data.get('email')
    partial_password = data.get('partial_password')

    try:
        conn = sqlite3.connect('db_login.db')
        cursor = conn.cursor()

        cursor.execute("SELECT senha FROM usuarios WHERE email = ?", (email,))
        user_data = cursor.fetchone()

        if user_data:
            stored_password = user_data[0]
            if stored_password.startswith(partial_password):
                return jsonify({"valid": True}), 200
            else:
                return jsonify({"valid": False}), 400
        else:
            return jsonify({"valid": False}), 400

    except sqlite3.Error as e:
        return jsonify({"error": f"Error checking password: {e}"}), 500
    finally:
        if conn:
            conn.close()
