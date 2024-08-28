from flask import Blueprint, render_template, request, redirect, url_for

funcionarios_bp = Blueprint('veiculos', __name__, template_folder='templates')

@funcionarios_bp.route('/criar', methods=['POST'])
def cadastrar_funcionario():
    pass

@funcionarios_bp.route('/buscar', methods=['GET'])
def buscar_funcionario():
    pass

@funcionarios_bp.route('/buscar/id', methods=['GET'])
def buscar_por_id():
    pass

@funcionarios_bp.route('/buscar/id_revendedora', methods=['GET'])
def buscar_por_revendedora():
    pass