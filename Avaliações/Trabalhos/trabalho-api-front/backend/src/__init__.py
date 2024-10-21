from flask import Flask
from db.database import criar_banco_de_dados
#Cria o app flask e onde fica definido as rotas inicias tbm
def create_app(config_class='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from .routes.usuarios_router import usuarios_bp
    from .routes.livros_router import livros_bp

    app.register_blueprint(usuarios_bp, url_prefix='/usuarios')    
    app.register_blueprint(livros_bp, url_prefix='/livros')    
    with app.app_context():
        criar_banco_de_dados()

    return app

