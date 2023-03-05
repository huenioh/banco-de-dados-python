from database.connect import ConnectDataBase
from modulos.aluguel.sql_aluguel import SQLAluguel
from modulos.aluguel.model_aluguel import Aluguel

class DaoAluguel:

    def __init__(self):
        self.connect = ConnectDataBase().get_instance()

    def salvar_aluguel(self, aluguel):
        cursor = self.connect.cursor()
        cursor.execute(SQLAluguel._SCRIPT_INSERT, (aluguel.id_livro, aluguel.id_cliente, aluguel.data_aluguel, aluguel.data_devolucao))
        self.connect.commit()
        id = cursor.fetchone()
        return id

    def get_alugueis(self, busca=None):
        cursor = self.connect.cursor()
        sql = SQLAluguel._SELECT_ALL
        cursor.execute(sql)

        alugueis = []
        coluns_name = [desc[0] for desc in cursor.description]
        for aluguel in cursor.fetchall():
            data = dict(zip(coluns_name, aluguel))
            alugueis.append(Aluguel(**data).get_json())
        return alugueis

    def get_alugueis_by_id(self, id):
        cursor = self.connect.cursor()
        cursor.execute(SQLAluguel._SELECT_ID, (str(id)))
        aluguel = cursor.fetchone()
        if not aluguel:
            return None
        else:
            coluns_name = [desc[0] for desc in cursor.description]
            data = dict(zip(coluns_name, aluguel))
            return Aluguel(**data)

    def delete_aluguel(self, id):
        cursor = self.connect.cursor()
        cursor.execute(SQLAluguel._DELETE_BY_ID, str(id))
        self.connect.commit()

    def atualizar_aluguel(self, aluguel):
        cursor = self.connect.cursor()
        cursor.execute(SQLAluguel._UPDATE_BY_ID, (aluguel.id_livro, aluguel.id_cliente, aluguel.data_aluguel, aluguel.data_devolucao, aluguel.id))
        self.connect.commit()
        return True