from database.connect import ConnectDataBase
from modulos.livro.sql_livro import SQLLivro
from modulos.livro.model_livro import Livro


class DaoLivro():

    def __init__(self):
        self.connect = ConnectDataBase().get_instance()

    def salvar(self, livro):
        cursor = self.connect.cursor()
        cursor.execute(SQLLivro._SCRIPT_INSET, (livro.nome, livro.autor, livro.ano_publicacao, livro.codigo_barras))
        self.connect.commit()
        id = cursor.fetchone()
        return id

    def get_livros(self, busca=None):
        cursor = self.connect.cursor()
        sql = SQLLivro._SELECT_BUSCA.format(SQLLivro._NOME_TABELA, busca) if busca else SQLLivro._SELECT_ALL
        cursor.execute(sql)

        livros = []
        coluns_name = [desc[0] for desc in cursor.description]
        for livro in cursor.fetchall():
            data = dict(zip(coluns_name, livro))
            livros.append(Livro(**data).get_json())
        return livros

    def get_livros_by_id(self, id):
        cursor = self.connect.cursor()
        cursor.execute(SQLLivro._SELECT_ID, (str(id)))
        livro = cursor.fetchone()
        if not livro:
            return None
        else:
            coluns_name = [desc[0] for desc in cursor.description]
            data = dict(zip(coluns_name, livro))
            return Livro(**data)

    def get_livros_by_autor(self, autor):
        cursor = self.connect.cursor()
        cursor.execute(SQLLivro._SELECT_AUTOR, ('%' + autor + '%',))
        livros_querry = cursor.fetchall()
        if not livros_querry:
            return None
        else:
            livros = []
            coluns_name = [desc[0] for desc in cursor.description]
            for livro in livros_querry:
                data = dict(zip(coluns_name, livro))
                livros.append(Livro(**data))
            return livros

    def get_livros_by_ano(self, ano):
        cursor = self.connect.cursor()
        cursor.execute(SQLLivro._SELECT_ANO, ('%' + ano + '%',))
        livros_querry = cursor.fetchall()
        if not livros_querry:
            return None
        else:
            livros = []
            coluns_name = [desc[0] for desc in cursor.description]
            for livro in livros_querry:
                data = dict(zip(coluns_name, livro))
                livros.append(Livro(**data))
            return livros

    def delete_livro(self, id):
        cursor = self.connect.cursor()
        cursor.execute(SQLLivro._DELETE_BY_ID, str(id))
        self.connect.commit()

    def atualizar_livro(self, livro):
        cursor = self.connect.cursor()
        cursor.execute(SQLLivro._UPDATE_BY_ID, (livro.nome, livro.autor, livro.ano_publicacao, livro.codigo_barras, livro.id))
        self.connect.commit()
        return True