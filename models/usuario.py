class Usuario:
    def __init__(self, id=None, nome=None, email=None):
        self.id = id
        self.nome = nome
        self.email = email

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "email": self.email}
