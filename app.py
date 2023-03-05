from flask import *
from database.connect import ConnectDataBase
from modulos.livro.model_livro import Livro
from modulos.livro.dao_livro import DaoLivro
from modulos.cliente.model_cliente import Cliente
from modulos.cliente.dao_cliente import DaoCliente
from modulos.aluguel.model_aluguel import Aluguel
from modulos.aluguel.dao_aluguel import DaoAluguel

from modulos.cliente.validador_cpf import validate_cpf

app = Flask(__name__)
ConnectDataBase().init_table()

dao_livro = DaoLivro()
dao_cliente = DaoCliente()
dao_aluguel = DaoAluguel()


# ROTAS PARA LIVRO -----------------------------------------------------------------------------------------------------

@app.route('/livros/add/', methods=['POST'])
def add_livro():
    data_livro = dict(request.form)
    livro = Livro(**data_livro)
    id = dao_livro.salvar(livro)
    livro.id = id
    return make_response({'id' : livro.id,'nome' : livro.nome,'autor' : livro.autor, 'ano_publicacao': livro.ano_publicacao, 'codigo_barras': livro.codigo_barras})

@app.route('/livros/', methods=['GET'])
def get_livros():
    parametros = request.args
    busca = parametros.get('busca', None)
    livro = dao_livro.get_livros(busca)
    return make_response(jsonify(livro))

@app.route('/livros/<int:id>/', methods=['GET'])
def livro_id(id: int):
    livro = dao_livro.get_livros_by_id(id)
    if not livro:
        return Response({}, status=404)
    return make_response(jsonify(livro.get_json()))

@app.route('/livros/autor/', methods=['GET'])
def get_livros_autor():
    parametros = request.args
    busca = parametros.get('busca', None)
    livros = dao_livro.get_livros_by_autor(busca)
    livros_by_autor = []
    for data in livros:
        livros_by_autor.append(data.get_json())
    return make_response(jsonify(livros_by_autor))

@app.route('/livros/ano/', methods=['GET'])
def get_livros_ano():
    parametros = request.args
    busca = parametros.get('busca', None)
    livros = dao_livro.get_livros_by_ano(busca)
    livros_by_ano = []
    for data in livros:
        livros_by_ano.append(data.get_json())
    return make_response(jsonify(livros_by_ano))

@app.route('/livros/<int:id>/', methods=['DELETE'])
def delete_livro(id: int):
    livro = dao_livro.get_livros_by_id(id)
    if livro:
        return Response(dao_livro.delete_livro(id), status=202)
    return Response({'Livro nao encontrado'}, status=404)

@app.route('/livros/<int:id>/', methods=['PUT'])
def atualizar_livro(id: int):
    data_livro = dict(request.form)
    livro = dao_livro.get_livros_by_id(id)
    if not livro:
        return Response({'Livro nao encontrado'}, status=404)
    livro.nome = data_livro.get('nome')
    livro.autor = data_livro.get('autor')
    livro.ano_publicacao = data_livro.get('ano_publicacao')
    livro.codigo_barras = data_livro.get('codigo_barras')
    dao_livro.atualizar_livro(livro)
    return make_response(jsonify(livro.get_json()))

# ROTAS PARA CLIENTE ---------------------------------------------------------------------------------------------------

@app.route('/clientes/add/', methods=['POST'])
def add_cliente():
    data_cliente = dict(request.form)
    if validate_cpf(data_cliente.get('cpf')):
        cliente = Cliente(**data_cliente)
        id = dao_cliente.salvar_cliente(cliente)
        cliente.id = id
        return make_response({'id' : cliente.id, 'nome' : cliente.nome, 'email' : cliente.email, 'cpf' : cliente.cpf})
    return Response({'CPF invalido'}, status=404)

@app.route('/clientes/', methods=['GET'])
def get_clientes():
    parametros = request.args
    busca = parametros.get('busca', None)
    cliente = dao_cliente.get_clientes(busca)
    return make_response(jsonify(cliente))

@app.route('/clientes/<int:id>/', methods=['GET'])
def cliente_id(id: int):
    cliente = dao_cliente.get_clientes_by_id(id)
    if not cliente:
        return Response({}, status=404)
    return make_response(jsonify(cliente.get_json()))

@app.route('/clientes/email/', methods=['GET'])
def clientes_email():
    parametros = request.args
    busca = parametros.get('busca', None)
    cliente = dao_cliente.get_clientes_by_email(busca)
    if not cliente:
        return Response({}, status=404)
    return make_response(jsonify(cliente.get_json()))

@app.route('/clientes/cpf/', methods=['GET'])
def clientes_cpf():
    parametros = request.args
    busca = parametros.get('busca', None)
    cliente = dao_cliente.get_clientes_by_cpf(busca)
    if not cliente:
        return Response({}, status=404)
    return make_response(jsonify(cliente.get_json()))

@app.route('/clientes/<int:id>/', methods=['DELETE'])
def delete_cliente(id: int):
    cliente = dao_cliente.get_clientes_by_id(id)
    if cliente:
        return Response(dao_cliente.delete_cliente(id), status=202)
    return Response({'Cliente nao encontrado'}, status=404)

@app.route('/clientes/<int:id>/', methods=['PUT'])
def atualizar_cliente(id: int):
    data_cliente = dict(request.form)
    cliente = dao_cliente.get_clientes_by_id(id)
    if not cliente:
        return Response({'Cliente nao encontrado'}, status=404)
    cliente.nome = data_cliente.get('nome')
    cliente.email = data_cliente.get('email')
    cliente.cpf = data_cliente.get('cpf')
    dao_cliente.atualizar_cliente(cliente)
    return make_response(jsonify(cliente.get_json()))


# ROTAS PARA ALUGUEL ---------------------------------------------------------------------------------------------------

@app.route('/alugueis/add/', methods=['POST'])
def add_aluguel():
    data_aluguel = dict(request.form)
    aluguel = Aluguel(**data_aluguel)
    livro = dao_livro.get_livros_by_id(aluguel.id_livro)
    cliente = dao_cliente.get_clientes_by_id(aluguel.id_cliente)
    if livro and cliente:
        id = dao_aluguel.salvar_aluguel(aluguel)
        aluguel.id = id
        return make_response({'id': aluguel.id, 'id_livro': aluguel.id_livro,'id_cliente': aluguel.id_cliente,'data_aluguel': aluguel.data_aluguel,'data_devolucao': aluguel.data_devolucao})
    return Response({'Livro ou Cliente nao encontrado'}, status=404)


@app.route('/alugueis/', methods=['GET'])
def get_alugueis():
    parametros = request.args
    busca = parametros.get('busca', None)
    aluguel = dao_aluguel.get_alugueis(busca)
    return make_response(jsonify(aluguel))

@app.route('/alugueis/<int:id>/', methods=['GET'])
def aluguel_id(id: int):
    aluguel = dao_aluguel.get_alugueis_by_id(id)
    if not aluguel:
        return Response({}, status=404)
    return make_response(jsonify(aluguel.get_json()))

@app.route('/alugueis/<int:id>/', methods=['DELETE'])
def delete_aluguel(id: int):
    aluguel = dao_aluguel.get_alugueis_by_id(id)
    if aluguel:
        return Response(dao_aluguel.delete_aluguel(id), status=202)
    return Response({'Aluguel nao encontrado'}, status=404)

@app.route('/alugueis/<int:id>/', methods=['PUT'])
def atualizar_aluguel(id: int):
    data_aluguel = dict(request.form)
    livro = dao_livro.get_livros_by_id(data_aluguel.get('id_livro'))
    cliente = dao_cliente.get_clientes_by_id(data_aluguel.get('id_cliente'))
    if livro and cliente:
        aluguel = dao_aluguel.get_alugueis_by_id(id)
        if not aluguel:
            return Response({'Cliente nao encontrado'}, status=404)
        aluguel.id_livro = data_aluguel.get('id_livro')
        aluguel.id_cliente = data_aluguel.get('id_cliente')
        aluguel.data_aluguel = data_aluguel.get('data_aluguel')
        aluguel.data_devolucao = data_aluguel.get('data_devolucao')
        dao_aluguel.atualizar_aluguel(aluguel)
        return make_response(jsonify(aluguel.get_json()))
    return Response({'Livro ou Cliente nao encontrado'}, status=404)

app.run()