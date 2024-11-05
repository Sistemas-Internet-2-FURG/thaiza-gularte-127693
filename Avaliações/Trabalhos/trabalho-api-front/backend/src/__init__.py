from flask import Flask
from flask_cors import CORS
from db.database import criar_banco_de_dados
#Cria o app flask e onde fica definido as rotas inicias tbm
def create_app():
    
    app = Flask(__name__)
    CORS(app) 
    
    from .routes.usuarios_router import usuarios_bp
    from .routes.livros_router import livros_bp
    from .routes.favoritos_router import favoritos_bp
    from .routes.comentarios_router import comentarios_bp

    app.register_blueprint(usuarios_bp, url_prefix='/usuarios')   
    app.register_blueprint(livros_bp, url_prefix='/livros')    
    app.register_blueprint(favoritos_bp, url_prefix='/favoritos')
    app.register_blueprint(comentarios_bp, url_prefix='/comentarios')

    with app.app_context():
        criar_banco_de_dados()

    return app

