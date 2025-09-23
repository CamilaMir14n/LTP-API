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
