from flask import Flask, jsonify
from utils.db import close_connection
from routes.usuario_routes import usuario_bp
from routes.filho_routes import filho_bp
from routes.atividade_routes import atividade_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(usuario_bp)
    app.register_blueprint(filho_bp)
    app.register_blueprint(atividade_bp)
    close_connection(app)

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "NOT_FOUND", "message": "Rota não encontrada"}), 404

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
