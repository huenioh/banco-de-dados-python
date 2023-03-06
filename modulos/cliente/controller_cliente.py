from flask import Blueprint, request, make_response, Response, jsonify
from modulos.cliente.validador_cpf import validate_cpf
from modulos.cliente.model_cliente import Cliente
from modulos.cliente.dao_cliente import DaoCliente

app_cliente = Blueprint('app_cliente', __name__)

dao_cliente = DaoCliente()

@app_cliente.route('/clientes/add/', methods=['POST'])
def add_cliente():
    data_cliente = dict(request.form)
    if validate_cpf(data_cliente.get('cpf')):
        cliente = Cliente(**data_cliente)
        id = dao_cliente.salvar_cliente(cliente)
        cliente.id = id
        return make_response({'id' : cliente.id, 'nome' : cliente.nome, 'email' : cliente.email, 'cpf' : cliente.cpf})
    return Response({'CPF invalido'}, status=404)

@app_cliente.route('/clientes/', methods=['GET'])
def get_clientes():
    parametros = request.args
    busca = parametros.get('busca', None)
    cliente = dao_cliente.get_clientes(busca)
    return make_response(jsonify(cliente))

@app_cliente.route('/clientes/<int:id>/', methods=['GET'])
def cliente_id(id: int):
    cliente = dao_cliente.get_clientes_by_id(id)
    if not cliente:
        return Response({}, status=404)
    return make_response(jsonify(cliente.get_json()))

@app_cliente.route('/clientes/email/', methods=['GET'])
def clientes_email():
    parametros = request.args
    busca = parametros.get('busca', None)
    cliente = dao_cliente.get_clientes_by_email(busca)
    if not cliente:
        return Response({}, status=404)
    return make_response(jsonify(cliente.get_json()))

@app_cliente.route('/clientes/cpf/', methods=['GET'])
def clientes_cpf():
    parametros = request.args
    busca = parametros.get('busca', None)
    cliente = dao_cliente.get_clientes_by_cpf(busca)
    if not cliente:
        return Response({}, status=404)
    return make_response(jsonify(cliente.get_json()))

@app_cliente.route('/clientes/<int:id>/', methods=['DELETE'])
def delete_cliente(id: int):
    cliente = dao_cliente.get_clientes_by_id(id)
    if cliente:
        return Response(dao_cliente.delete_cliente(id), status=202)
    return Response({'Cliente nao encontrado'}, status=404)

@app_cliente.route('/clientes/<int:id>/', methods=['PUT'])
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

