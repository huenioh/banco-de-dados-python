from flask import Blueprint, request, make_response, Response, jsonify
from modulos.aluguel.model_aluguel import Aluguel
from modulos.aluguel.dao_aluguel import DaoAluguel
from modulos.livro.dao_livro import DaoLivro
from modulos.cliente.dao_cliente import DaoCliente

app_aluguel = Blueprint('app_aluguel', __name__)

dao_aluguel = DaoAluguel()
dao_livro = DaoLivro()
dao_cliente = DaoCliente()

@app_aluguel.route('/alugueis/add/', methods=['POST'])
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


@app_aluguel.route('/alugueis/', methods=['GET'])
def get_alugueis():
    parametros = request.args
    busca = parametros.get('busca', None)
    aluguel = dao_aluguel.get_alugueis(busca)
    return make_response(jsonify(aluguel))

@app_aluguel.route('/alugueis/<int:id>/', methods=['GET'])
def aluguel_id(id: int):
    aluguel = dao_aluguel.get_alugueis_by_id(id)
    if not aluguel:
        return Response({}, status=404)
    return make_response(jsonify(aluguel.get_json()))

@app_aluguel.route('/alugueis/<int:id>/', methods=['DELETE'])
def delete_aluguel(id: int):
    aluguel = dao_aluguel.get_alugueis_by_id(id)
    if aluguel:
        return Response(dao_aluguel.delete_aluguel(id), status=202)
    return Response({'Aluguel nao encontrado'}, status=404)

@app_aluguel.route('/alugueis/<int:id>/', methods=['PUT'])
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