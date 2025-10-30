from flask import Blueprint, request, jsonify, current_app
from services.usuario_service import UsuarioService
from dao.usuario_dao import UsuarioDAO
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
import datetime

auth_bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()
jwt_blacklist = set()

@auth_bp.record_once
def init_bcrypt(state):
    bcrypt.init_app(state.app)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    nome = data.get('nome'); email = data.get('email'); password = data.get('password')
    if not nome or not email or not password:
        return jsonify({'msg': 'nome, email e password são obrigatórios'}), 400
    pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    usuario, err = UsuarioService.criar_usuario(nome, email, pw_hash)
    if err == 'USR001':
        return jsonify({'msg': 'email já cadastrado'}), 409
    return jsonify({'msg': 'usuário criado', 'user': usuario.to_dict()}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email'); password = data.get('password')
    if not email or not password:
        return jsonify({'msg': 'email e password são obrigatórios'}), 400
    user = UsuarioDAO.buscar_por_email(email)
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({'msg': 'credenciais inválidas'}), 401
    expires = datetime.timedelta(seconds=current_app.config.get('JWT_ACCESS_TOKEN_EXPIRES', 3600))
    access_token = create_access_token(identity=user.id, expires_delta=expires)
    return jsonify({'access_token': access_token}), 200

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    jwt_blacklist.add(jti)
    return jsonify({'msg': 'token invalidado (logout)'}), 200

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = UsuarioDAO.buscar_por_id(user_id)
    if not user:
        return jsonify({'msg': 'usuário não encontrado'}), 404
    return jsonify(user.to_dict()), 200

def is_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload.get('jti')
    return jti in jwt_blacklist
