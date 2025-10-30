from dao.usuario_dao import UsuarioDAO
from dao.filho_dao import FilhoDAO
from models.usuario import Usuario

class UsuarioService:
    @staticmethod
    def criar_usuario(nome, email, password):
        uid, err = UsuarioDAO.criar(nome, email, password)
        if err:
            return None, err
        usuario = Usuario(uid, nome, email, password)
        return usuario, None


    @staticmethod
    def listar_usuarios():
        return UsuarioDAO.listar_todos()

    @staticmethod
    def buscar_usuario(id):
        return UsuarioDAO.buscar_por_id(id)

    @staticmethod
    def atualizar_usuario(id, nome, email):
        usuario, err = UsuarioDAO.atualizar(id, nome, email)
        if err:
            return None, err
        return usuario, None

    @staticmethod
    def deletar_usuario(id):
        sucesso, err = UsuarioDAO.deletar(id)
        if err:
            return False, err
        return True, None

    @staticmethod
    def deletar_usuario(id):
        sucesso, err = UsuarioDAO.deletar(id)
        if err:
            return False, err
        return True, None
