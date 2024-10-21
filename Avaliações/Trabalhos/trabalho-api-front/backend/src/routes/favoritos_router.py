import sqlite3
from flask import Blueprint, jsonify, render_template, request, redirect, url_for
import requests

favoritos_bp = Blueprint('favoritos', __name__, template_folder='templates')

@favoritos_bp.route('/criar', methods=['POST'])
def adicionar_favorito():
    pass

@favoritos_bp.route('/buscar', methods=['GET'])
def buscar_favoritos():
    pass

@favoritos_bp.route('/buscar/id', methods=['GET'])
def buscar_favorito_id():
    pass

