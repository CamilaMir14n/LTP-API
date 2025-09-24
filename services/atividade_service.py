from dao.atividade_dao import AtividadeDAO
from models.atividade import Atividade

class AtividadeService:
    @staticmethod
    def buscar_atividade(id):
        return AtividadeDAO.buscar_por_id(id)

    @staticmethod
    def atualizar_atividade(id, filho_id, titulo, descricao, status):
        atividade, err = AtividadeDAO.atualizar(id, filho_id, titulo, descricao, status)
        if err:
            return None, err
        return atividade, None

    @staticmethod
    def deletar_atividade(id):
        sucesso, err = AtividadeDAO.deletar(id)
        if err:
            return False, err
        return True, None

    @staticmethod
    def criar_atividade(filho_id, titulo, descricao=None, status='pendente'):
        aid, err = AtividadeDAO.criar(filho_id, titulo, descricao, status)
        if err:
            return None, err
        return Atividade(aid, filho_id, titulo, descricao, status), None

    @staticmethod
    def listar_atividades():
        return AtividadeDAO.listar_todos()

    @staticmethod
    def listar_por_filho(filho_id):
        return AtividadeDAO.listar_por_filho(filho_id)
