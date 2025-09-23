class Filho:
    def __init__(self, id=None, usuario_id=None, nome=None, idade=None):
        self.id = id
        self.usuario_id = usuario_id
        self.nome = nome
        self.idade = idade

    def to_dict(self):
        return {"id": self.id, "usuario_id": self.usuario_id, "nome": self.nome, "idade": self.idade}
