from flask import Flask, redirect, url_for
from flask_cors import CORS
from db.database import criar_banco_de_dados
#Cria o app flask e onde fica definido as rotas inicias tbm

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Registra o blueprint de usuários
    from .routes.usuario_routes import usuarios_bp
    app.register_blueprint(usuarios_bp, url_prefix='/')

    # Nova rota para redirecionar para a página de cadastro
    @app.route('/')
    def home():
        return redirect(url_for('usuarios.cadastrar_usuario'))  # 'usuarios.cadastrar_usuario' é o nome da função da rota de cadastro

    with app.app_context():
        criar_banco_de_dados()

    return app
