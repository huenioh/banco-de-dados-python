class SQLLivro:
    _NOME_TABELA = 'livros'
    _SCRIPT_CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_NOME_TABELA} (' \
                           f'id serial primary key, ' \
                           f'nome varchar(100) NOT NULL, ' \
                           f'autor varchar(100) NOT NULL, ' \
                           f'ano_publicacao varchar(4) NOT NULL, ' \
                           f'codigo_barras varchar(13) NOT NULL)'
    _SCRIPT_INSET = f'INSERT INTO {_NOME_TABELA}(nome, autor, ano_publicacao, codigo_barras) ' \
                    f'values(%s, %s, %s, %s) RETURNING id'
    _SELECT_ALL = f'SELECT * FROM {_NOME_TABELA}'
    _SELECT_ID = f'SELECT * FROM {_NOME_TABELA} WHERE ID=%s'
    _SELECT_AUTOR = f'SELECT * FROM {_NOME_TABELA} WHERE autor ILIKE %s'
    _SELECT_ANO = f'SELECT * FROM {_NOME_TABELA} WHERE ano_publicacao ILIKE %s'
    _SELECT_BUSCA = "SELECT * FROM {} where codigo_barras ILIKE '%{}%'"

    _UPDATE_BY_ID = f'UPDATE {_NOME_TABELA} SET nome=%s, autor=%s, ano_publicacao=%s, codigo_barras=%s ' \
                    f'WHERE id=%s'
    _DELETE_BY_ID = F'DELETE FROM {_NOME_TABELA} WHERE ID=%s'