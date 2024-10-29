from flask import redirect, url_for
from src import create_app

if __name__ == '__main__':
    create_app().run(debug=True)
