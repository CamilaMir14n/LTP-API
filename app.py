from flask import Flask, jsonify
from utils.db import close_connection
from routes.usuario_routes import usuario_bp
from routes.filho_routes import filho_bp
from routes.atividade_routes import atividade_bp
from flask_jwt_extended import JWTManager
from routes.auth_routes import auth_bp, is_token_revoked

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'chave-secreta-forte'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(usuario_bp)
    app.register_blueprint(filho_bp)
    app.register_blueprint(atividade_bp)
    close_connection(app)

    jwt = JWTManager(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload):
        return is_token_revoked(jwt_header, jwt_payload)


    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "NOT_FOUND", "message": "Rota não encontrada"}), 404

    return app

import os
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port = os.environ.get('PORT', 3000), debug=True)