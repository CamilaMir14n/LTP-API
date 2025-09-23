class Atividade:
    def __init__(self, id=None, filho_id=None, titulo=None, descricao=None, status=None):
        self.id = id
        self.filho_id = filho_id
        self.titulo = titulo
        self.descricao = descricao
        self.status = status

    def to_dict(self):
        return {"id": self.id, "filho_id": self.filho_id, "titulo": self.titulo, "descricao": self.descricao, "status": self.status}
