class Cliente(object):
    def __init__(self, nome, email, cpf, id = None):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.id = id

    def __str__(self):
        return f'ID: {self.id} - Nome: {self.nome} - Email: {self.email} - CPF: {self.cpf}'

    def get_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'cpf': self.cpf
        }