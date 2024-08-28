import sqlite3
from flask import Blueprint, render_template, request, redirect, url_for
import requests

revendedoras_bp = Blueprint('revendedoras', __name__, template_folder='app/templates')

@revendedoras_bp.route('/criar', methods=['POST', 'GET'])
def cadastrar_revendedora():
    if request.method == 'POST':
        nome_estabelecimento = request.form['nome_estabelecimento']
        email = request.form['email']
        senha = request.form['senha']
        cnpj = request.form['cnpj']

       # Conectando ao banco de dados e inserindo os dados
        conn = sqlite3.connect('db_api_flask.db')
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO revendedoras (nome_estabelecimento, email, senha, cnpj)
                VALUES (?, ?, ?, ?)
            ''', (nome_estabelecimento, email, senha, cnpj))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao inserir os dados: {e}")
        finally:
            conn.close()
            return render_template('revendedoras/aviso_sucesso.html')

    elif request.method == 'GET':
        return render_template('revendedoras/criar_revendedora.html')

@revendedoras_bp.route('/acessar', methods=['POST','GET'])
def acessar_cadastro():
    if(request.method == 'POST'):
        email = request.form['email']
        senha = request.form['senha']

        conn = sqlite3.connect('db_api_flask.db')
        cursor = conn.cursor()

        try:
            cursor.execute('''
                SELECT id,nome_estabelecimento,email,senha FROM revendedoras WHERE email = ? AND senha = ?
            ''', (email, senha))
            usuario = cursor.fetchone()
            if usuario:
                id, nome_estabelecimento,_,_ = usuario
                return redirect(url_for('revendedoras.revendedora_logada', id=id, nome_estabelecimento=nome_estabelecimento))

            else:
                return "Email ou senha incorretos", 401
        except sqlite3.Error as e:
            print(f"Erro ao acessar o banco de dados: {e}")
            return "Erro ao acessar o banco de dados", 500
        finally:
            conn.close()
    elif request.method == 'GET':
        return render_template('revendedoras/acesso_revendedora.html')

@revendedoras_bp.route('/logado/<int:id>/<string:nome_estabelecimento>', methods=['GET'])
def revendedora_logada(id,nome_estabelecimento):
    response = requests.get(f'http://localhost:5000/veiculos/buscar/{id}')
    veiculos = response.json()                
    return render_template('revendedoras/tela_inicial.html', id=id, nome_estabelecimento = nome_estabelecimento, veiculos=veiculos)

@revendedoras_bp.route('/buscar', methods=['GET'])
def buscar_revendedoras():
    pass

@revendedoras_bp.route('/buscar/id', methods=['GET'])
def buscar_por_id():
    pass

