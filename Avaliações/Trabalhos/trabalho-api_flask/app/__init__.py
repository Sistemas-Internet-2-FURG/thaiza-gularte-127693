from flask import Flask
from .database.database import criar_banco_de_dados
#Cria o app flask e onde fica definido as rotas inicias tbm
def create_app(config_class='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from .routes.revendedoras.revendedoras_router import revendedoras_bp
    from .routes.veiculos.veiculos_router import veiculos_bp

    app.register_blueprint(revendedoras_bp, url_prefix='/revendedoras')    
    app.register_blueprint(veiculos_bp, url_prefix='/veiculos')    
    with app.app_context():
        criar_banco_de_dados()

    return app

