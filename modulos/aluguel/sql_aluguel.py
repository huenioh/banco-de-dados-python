class SQLAluguel:
    _NOME_TABELA = 'alugueis'
    _SCRIPT_CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_NOME_TABELA} (' \
                           'id SERIAL PRIMARY KEY,' \
                           'id_livro INTEGER NOT NULL,' \
                           'id_cliente INTEGER NOT NULL,' \
                           'data_aluguel DATE NOT NULL,' \
                           'data_devolucao DATE,' \
                           'FOREIGN KEY (id_livro) REFERENCES livros(id),' \
                           'FOREIGN KEY (id_cliente) REFERENCES clientes(id))'
    _SCRIPT_INSERT = f'INSERT INTO {_NOME_TABELA}(id_livro, id_cliente, data_aluguel, data_devolucao) ' \
                     f'values(%s, %s, %s, %s) RETURNING id'
    _SELECT_ALL = f'SELECT * FROM {_NOME_TABELA}'
    _SELECT_ID = f'SELECT * FROM {_NOME_TABELA} WHERE ID=%s'
    _UPDATE_BY_ID = f'UPDATE {_NOME_TABELA} SET id_livro=%s, id_cliente=%s, data_aluguel=%s, data_devolucao=%s ' \
                    f'WHERE id=%s'
    _DELETE_BY_ID = F'DELETE FROM {_NOME_TABELA} WHERE ID=%s'