from flask_jwt_extended import verify_jwt_in_request
from flask import jsonify

def protect_blueprint(bp):
    @bp.before_request
    def _protect():
        #try:
            verify_jwt_in_request()
        #except Exception:
        #    return jsonify({"msg": "Token JWT obrigatório ou inválido"}), 401
