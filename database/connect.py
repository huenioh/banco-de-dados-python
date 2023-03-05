import psycopg2
from modulos.livro.sql_livro import SQLLivro
from modulos.cliente.sql_cliente import SQLCliente
from modulos.aluguel.sql_aluguel import SQLAluguel


class ConnectDataBase:
    def __init__(self):
        self._connect = psycopg2.connect(
            host="localhost",
            database="biblioteca",
            user="postgres",
            password="admin"
        )

    def get_instance(self):
        return self._connect

    def init_table(self):
        cursor = self._connect.cursor()
        cursor.execute(SQLLivro._SCRIPT_CREATE_TABLE)
        cursor.execute(SQLCliente._SCRIPT_CREATE_TABLE)
        cursor.execute(SQLAluguel._SCRIPT_CREATE_TABLE)
        self._connect.commit()