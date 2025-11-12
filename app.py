import os
from flask import Flask, jsonify
from utils.db import close_connection
from routes.usuario_routes import usuario_bp
from routes.filho_routes import filho_bp
from routes.atividade_routes import atividade_bp
from flask_jwt_extended import JWTManager
from routes.auth_routes import auth_bp, is_token_revoked

from init_db import init_db

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'chave-padrao-local')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES', 3600))
    if not os.path.exists('artistick.db'):
        print("artistick.db não encontrado — criando com init_db()")
        init_db()
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
    app.run(host="0.0.0.0", port=init('PORT', 3000), debug=True)