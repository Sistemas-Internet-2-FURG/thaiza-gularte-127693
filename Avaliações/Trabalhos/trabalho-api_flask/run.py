from flask import redirect, url_for
from app import create_app

app = create_app()

@app.route('/')
def home():
    return redirect(url_for('revendedoras.acessar_cadastro'))

if __name__ == '__main__':
    app.run(debug=True)
