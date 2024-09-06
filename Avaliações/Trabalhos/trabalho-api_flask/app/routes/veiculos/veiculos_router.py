import sqlite3
from flask import Blueprint, jsonify, render_template, request, redirect, url_for

veiculos_bp = Blueprint('veiculos', __name__, template_folder='templates')

@veiculos_bp.route('/criar/<int:id>/<string:nome_estabelecimento>', methods=['POST', 'GET'])
def cadastrar_veiculo(id,nome_estabelecimento):
    if(request.method == 'POST'):
        nome = request.form['nome']
        marca = request.form['marca']
        modelo = request.form['modelo']
        valor = request.form['valor']
        imagem = request.form['imagem']

        conn = sqlite3.connect('db_api_flask.db')
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO veiculos (id_revendedora, nome, marca, modelo,valor,imagem)
                VALUES (?, ?, ?, ?, ?,?)
            ''', (id,nome, marca,modelo,valor,imagem))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao inserir os dados: {e}")
        finally:
            conn.close()
            return  render_template('veiculos/aviso_sucesso.html', id= id, nome_estabelecimento=nome_estabelecimento)

    elif request.method == 'GET':
        return render_template('veiculos/criar_veiculo.html',id=id,nome_estabelecimento=nome_estabelecimento)

@veiculos_bp.route('/buscar/<int:id>', methods=['GET'])
def buscar_veiculos(id):
    conn = sqlite3.connect('db_api_flask.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            SELECT id, id_revendedora, nome, marca, modelo, valor, imagem
            FROM veiculos WHERE id_revendedora = ?
        ''', (id,))
        veiculos = cursor.fetchall()

        veiculos_list = [
            {
                'id': veiculo[0],
                'id_revendedora': veiculo[1],
                'nome': veiculo[2],
                'marca': veiculo[3],
                'modelo': veiculo[4],
                'valor': veiculo[5],
                'imagem': veiculo[6]
            }
            for veiculo in veiculos
        ]

        return jsonify(veiculos_list)
    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")
        return jsonify({'error': 'Erro ao acessar o banco de dados'}), 500
    finally:
        conn.close()

@veiculos_bp.route('/<int:id>/<int:id_usuario>/<string:nome>', methods=['POST', 'GET'])
def editar_deletar(id, id_usuario,nome):
    conn = sqlite3.connect('db_api_flask.db')
    cursor = conn.cursor()

    # Método GET: Carregar os dados do veículo e renderizar o template de edição
    if request.method == 'GET':
        cursor.execute('SELECT id,nome,marca,modelo,valor,imagem  FROM veiculos WHERE id = ?', (id,))
        veiculo = cursor.fetchone()
        conn.close()
        
        if veiculo:
            # Mapeia os dados do veículo para um dicionário
            veiculo_dict = {
                'id': veiculo[0],
                'nome': veiculo[1],
                'marca': veiculo[2],
                'modelo': veiculo[3],
                'valor': veiculo[4],
                'imagem': veiculo[5]
            }
            return render_template('veiculos/editar_veiculo.html', veiculo=veiculo_dict, id=id_usuario, nome=nome)
        else:
            return "Veículo não encontrado", 404

    # Método POST: Processar o formulário de edição ou exclusão
    elif request.method == 'POST':
        method = request.form.get('_method')

        if method == 'PUT':
            nome = request.form['nome']
            marca = request.form['marca']
            modelo = request.form['modelo']
            valor = request.form['valor']
            imagem = request.form['imagem']

            try:
                cursor.execute('''
                    UPDATE veiculos SET nome = ?, marca = ?, modelo = ?, valor = ?, imagem = ? WHERE id = ?
                ''', (nome, marca, modelo, valor, imagem, id))
                conn.commit()
                return redirect(url_for('revendedoras.revendedora_logada',id=id_usuario, nome_estabelecimento=nome))
            except sqlite3.Error as e:
                print(f"Erro ao atualizar o veículo: {e}")
                return "Erro ao atualizar o veículo", 500
            finally:
                conn.close()

        elif method == 'DELETE':
            try:
                cursor.execute('''
                    DELETE FROM veiculos WHERE id = ?
                ''', (id,))
                conn.commit()
                return redirect(url_for('revendedoras.revendedora_logada',id=id_usuario, nome_estabelecimento=nome))
            except sqlite3.Error as e:
                print(f"Erro ao deletar o veículo: {e}")
                return "Erro ao deletar o veículo", 500
            finally:
                conn.close()


@veiculos_bp.route('/buscar/id', methods=['GET'])
def buscar_veiculo_por_id():
    pass

@veiculos_bp.route('/buscar/id_revendedora', methods=['GET'])
def buscar_por_revendedora():
    pass

