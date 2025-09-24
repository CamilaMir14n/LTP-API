from flask import Blueprint, request, jsonify
from services.atividade_service import AtividadeService

atividade_bp = Blueprint('atividades', __name__)

@atividade_bp.route('/atividades', methods=['POST'])
def criar_atividade():
    data = request.get_json()
    filho_id = data.get('filho_id')
    titulo = data.get('titulo')
    descricao = data.get('descricao')
    status = data.get('status', 'pendente')
    if not filho_id or not titulo:
        return jsonify({"error": "ATI002", "message": "filho_id e titulo são obrigatórios"}), 400
    atividade, err = AtividadeService.criar_atividade(filho_id, titulo, descricao, status)
    if err:
        return jsonify({"error": err, "message": "Filho inválido"}), 400
    return jsonify(atividade.to_dict()), 201

@atividade_bp.route('/atividades', methods=['GET'])
def listar_atividades():
    filho_id = request.args.get('filho')
    if filho_id:
        atividades = AtividadeService.listar_por_filho(filho_id)
        return jsonify([a.to_dict() for a in atividades]), 200
    atividades = AtividadeService.listar_atividades()
    return jsonify([a.to_dict() for a in atividades]), 200


# GET por ID
@atividade_bp.route('/atividades/<int:id>', methods=['GET'])
def buscar_atividade(id):
    a = AtividadeService.buscar_atividade(id)
    if not a:
        return jsonify({"error": "ATI404", "message": "Atividade não encontrada"}), 404
    return jsonify(a.to_dict()), 200

# PUT - Atualizar atividade
@atividade_bp.route('/atividades/<int:id>', methods=['PUT'])
def atualizar_atividade(id):
    data = request.get_json()
    filho_id = data.get('filho_id')
    titulo = data.get('titulo')
    descricao = data.get('descricao')
    status = data.get('status', 'pendente')
    if not filho_id or not titulo:
        return jsonify({"error": "ATI002", "message": "filho_id e titulo são obrigatórios"}), 400
    atividade, err = AtividadeService.atualizar_atividade(id, filho_id, titulo, descricao, status)
    if err == "ATI404":
        return jsonify({"error": err, "message": "Atividade não encontrada"}), 404
    if err == "ATI001":
        return jsonify({"error": err, "message": "Filho inválido"}), 400
    return jsonify(atividade.to_dict()), 200

# DELETE - Remover atividade
@atividade_bp.route('/atividades/<int:id>', methods=['DELETE'])
def deletar_atividade(id):
    sucesso, err = AtividadeService.deletar_atividade(id)
    if err == "ATI404":
        return jsonify({"error": err, "message": "Atividade não encontrada"}), 404
    return jsonify({"message": "Atividade deletada com sucesso"}), 200
