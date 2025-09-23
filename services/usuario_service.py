from dao.usuario_dao import UsuarioDAO
from dao.filho_dao import FilhoDAO
from models.usuario import Usuario

class UsuarioService:
    @staticmethod
    def criar_usuario(nome, email):
        uid, err = UsuarioDAO.criar(nome, email)
        if err:
            return None, err
        usuario = Usuario(uid, nome, email)
        return usuario, None

    @staticmethod
    def listar_usuarios():
        return UsuarioDAO.listar_todos()

    @staticmethod
    def buscar_usuario(id):
        return UsuarioDAO.buscar_por_id(id)
