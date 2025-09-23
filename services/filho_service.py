from dao.filho_dao import FilhoDAO
from models.filho import Filho

class FilhoService:
    @staticmethod
    def criar_filho(usuario_id, nome, idade):
        fid, err = FilhoDAO.criar(usuario_id, nome, idade)
        if err:
            return None, err
        return Filho(fid, usuario_id, nome, idade), None

    @staticmethod
    def listar_filhos_por_usuario(usuario_id):
        return FilhoDAO.listar_por_usuario(usuario_id)

    @staticmethod
    def buscar_filho(id):
        return FilhoDAO.buscar_por_id(id)
