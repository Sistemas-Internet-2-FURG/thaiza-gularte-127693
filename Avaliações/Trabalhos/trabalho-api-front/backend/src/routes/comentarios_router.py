import sqlite3
from flask import Blueprint, jsonify, render_template, request, redirect, url_for
import requests

comentarios_bp = Blueprint('comentarios', __name__, template_folder='templates')

@comentarios_bp.route('/criar', methods=['POST'])
def criar_comentario():
    pass

@comentarios_bp.route('/buscar', methods=['GET'])
def buscar_comentarios():
    pass

@comentarios_bp.route('/buscar/id', methods=['GET'])
def buscar_comentario_id():
    pass

