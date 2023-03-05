class Aluguel(object):
    def __init__(self, id_livro, id_cliente, data_aluguel, data_devolucao,id = None):
        self.id_livro = id_livro
        self.id_cliente = id_cliente
        self.data_aluguel = data_aluguel
        self.data_devolucao = data_devolucao
        self.id = id

    def __str__(self):
        return f'id_livro: {self.id_livro} - id_cliente: {self.id_cliente} - data_aluguel: {self.data_aluguel} - data_devolucao: {self.data_devolucao}'

    def get_json(self):
        return {
            'id': self.id,
            'id_livro': self.id_livro,
            'id_cliente': self.id_cliente,
            'data_aluguel': self.data_aluguel,
            'data_devolucao': self.data_devolucao
        }