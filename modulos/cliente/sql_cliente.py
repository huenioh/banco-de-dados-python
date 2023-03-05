class SQLCliente:
    _NOME_TABELA = 'clientes'
    _SCRIPT_CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_NOME_TABELA} (' \
                           f'id serial primary key, ' \
                           f'nome varchar(100) NOT NULL, ' \
                           f'email varchar(100) NOT NULL, ' \
                           f'cpf varchar(14) NOT NULL)'
    _SCRIPT_INSERT = f'INSERT INTO {_NOME_TABELA}(nome, email, cpf) ' \
                    f'values(%s, %s, %s) RETURNING id'
    _SELECT_ALL = f'SELECT * FROM {_NOME_TABELA}'
    _SELECT_ID = f'SELECT * FROM {_NOME_TABELA} WHERE ID=%s'
    _SELECT_EMAIL = "SELECT * FROM {} WHERE email ILIKE '%{}%'"
    _SELECT_CPF = "SELECT * FROM {} where cpf ILIKE '%{}%'"

    _UPDATE_BY_ID = f'UPDATE {_NOME_TABELA} SET nome=%s, email=%s, cpf=%s ' \
                    f'WHERE id=%s'
    _DELETE_BY_ID = F'DELETE FROM {_NOME_TABELA} WHERE ID=%s'