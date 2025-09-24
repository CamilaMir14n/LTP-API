from flask import Blueprint, request, jsonify
from services.usuario_service import UsuarioService

usuario_bp = Blueprint('usuarios', __name__)

# DELETE - Remover usuário
@usuario_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    sucesso, err = UsuarioService.deletar_usuario(id)
    if err == "USR404":
        return jsonify({"error": err, "message": "Usuário não encontrado"}), 404
    return jsonify({"message": "Usuário deletado com sucesso"}), 200
from flask import Blueprint, request, jsonify
from services.usuario_service import UsuarioService

@usuario_bp.route('/usuarios', methods=['POST'])
def criar_usuario():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')
    if not nome or not email:
        return jsonify({"error": "USR002", "message": "Nome e email são obrigatórios"}), 400
    usuario, err = UsuarioService.criar_usuario(nome, email)
    if err:
        return jsonify({"error": err, "message": "Email já cadastrado"}), 400
    return jsonify(usuario.to_dict()), 201

@usuario_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = UsuarioService.listar_usuarios()
    return jsonify([u.to_dict() for u in usuarios]), 200

@usuario_bp.route('/usuarios/<int:id>', methods=['GET'])
def buscar_usuario(id):
    u = UsuarioService.buscar_usuario(id)
    if not u:
        return jsonify({"error": "USR404", "message": "Usuário não encontrado"}), 404
    return jsonify(u.to_dict()), 200


# PUT - Atualizar usuário
@usuario_bp.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')
    if not nome or not email:
        return jsonify({"error": "USR002", "message": "Nome e email são obrigatórios"}), 400
    usuario, err = UsuarioService.atualizar_usuario(id, nome, email)
    if err == "USR404":
        return jsonify({"error": err, "message": "Usuário não encontrado"}), 404
    if err == "USR001":
        return jsonify({"error": err, "message": "Email já cadastrado"}), 400
    return jsonify(usuario.to_dict()), 200
