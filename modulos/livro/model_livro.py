class Livro(object):
    def __init__(self, nome, autor, ano_publicacao, codigo_barras, id = None):
        self.nome = nome
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.codigo_barras = codigo_barras
        self.id = id

    def __str__(self):
        return f'ID: {self.id} - Nome: {self.nome} - Autor: {self.autor} - Ano Pub.: {self.ano_publicacao} - Código de Barras: {self.codigo_barras}'

    def get_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'autor': self.autor,
            'ano_publicacao': self.ano_publicacao,
            'codigo_barras': self.codigo_barras
        }