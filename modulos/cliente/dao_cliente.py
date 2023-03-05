from database.connect import ConnectDataBase
from modulos.cliente.sql_cliente import SQLCliente
from modulos.cliente.validador_cpf import validate_cpf
from modulos.cliente.model_cliente import Cliente

class DaoCliente():

    def __init__(self):
        self.connect = ConnectDataBase().get_instance()

    def salvar_cliente(self, cliente):
        cursor = self.connect.cursor()
        validador = validate_cpf(cliente.cpf)
        cursor.execute(SQLCliente._SCRIPT_INSERT, (cliente.nome, cliente.email, cliente.cpf))
        self.connect.commit()
        id = cursor.fetchone()
        return id

    def get_clientes(self, busca=None):
        cursor = self.connect.cursor()
        sql = SQLCliente._SELECT_BUSCA.format(SQLCliente._NOME_TABELA, busca) if busca else SQLCliente._SELECT_ALL
        cursor.execute(sql)

        clientes = []
        coluns_name = [desc[0] for desc in cursor.description]
        for cliente in cursor.fetchall():
            data = dict(zip(coluns_name, cliente))
            clientes.append(Cliente(**data).get_json())
        return clientes

    def get_clientes_by_id(self, id):
        cursor = self.connect.cursor()
        cursor.execute(SQLCliente._SELECT_ID, (str(id)))
        cliente = cursor.fetchone()
        if not cliente:
            return None
        else:
            coluns_name = [desc[0] for desc in cursor.description]
            data = dict(zip(coluns_name, cliente))
            return Cliente(**data)

    def get_clientes_by_email(self, email):
        cursor = self.connect.cursor()
        cursor.execute(SQLCliente._SELECT_EMAIL.format(SQLCliente._NOME_TABELA, email))
        cliente = cursor.fetchone()
        if not cliente:
            return None
        else:
            coluns_name = [desc[0] for desc in cursor.description]
            data = dict(zip(coluns_name, cliente))
            return Cliente(**data)

    def get_clientes_by_cpf(self, cpf):
        cursor = self.connect.cursor()
        cursor.execute(SQLCliente._SELECT_CPF.format(SQLCliente._NOME_TABELA, cpf))
        cliente = cursor.fetchone()
        if not cliente:
            return None
        else:
            coluns_name = [desc[0] for desc in cursor.description]
            data = dict(zip(coluns_name, cliente))
            return Cliente(**data)

    def delete_cliente(self, id):
        cursor = self.connect.cursor()
        cursor.execute(SQLCliente._DELETE_BY_ID, str(id))
        self.connect.commit()

    def atualizar_cliente(self, cliente):
        cursor = self.connect.cursor()
        cursor.execute(SQLCliente._UPDATE_BY_ID, (cliente.nome, cliente.email, cliente.cpf, cliente.id))
        self.connect.commit()
        return True