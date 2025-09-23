from flask import Blueprint, request, jsonify
from services.filho_service import FilhoService

filho_bp = Blueprint('filhos', __name__)

@filho_bp.route('/filhos', methods=['POST'])
def criar_filho():
    data = request.get_json()
    usuario_id = data.get('usuario_id')
    nome = data.get('nome')
    idade = data.get('idade')
    if not usuario_id or not nome:
        return jsonify({"error": "FIL002", "message": "usuario_id e nome são obrigatórios"}), 400
    filho, err = FilhoService.criar_filho(usuario_id, nome, idade)
    if err:
        return jsonify({"error": err, "message": "Usuário inválido"}), 400
    return jsonify(filho.to_dict()), 201

@filho_bp.route('/filhos', methods=['GET'])
def listar_filhos():
    usuario_id = request.args.get('usuario')
    if usuario_id:
        filhos = FilhoService.listar_filhos_por_usuario(usuario_id)
        return jsonify([f.to_dict() for f in filhos]), 200
    return jsonify({"error": "FIL003", "message": "Parâmetro usuario é necessário"}), 400

@filho_bp.route('/filhos/<int:id>', methods=['GET'])
def buscar_filho(id):
    f = FilhoService.buscar_filho(id)
    if not f:
        return jsonify({"error": "FIL404", "message": "Filho não encontrado"}), 404
    return jsonify(f.to_dict()), 200
