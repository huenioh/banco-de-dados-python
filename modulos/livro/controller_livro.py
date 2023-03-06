from flask import Blueprint, request, make_response, Response, jsonify
from modulos.livro.model_livro import Livro
from modulos.livro.dao_livro import DaoLivro

app_livro = Blueprint('app_livro', __name__)

dao_livro = DaoLivro()

@app_livro.route('/livros/add/', methods=['POST'])
def add_livro():
    data_livro = dict(request.form)
    livro = Livro(**data_livro)
    id = dao_livro.salvar(livro)
    livro.id = id
    return make_response({'id' : livro.id,'nome' : livro.nome,'autor' : livro.autor, 'ano_publicacao': livro.ano_publicacao, 'codigo_barras': livro.codigo_barras})

@app_livro.route('/livros/', methods=['GET'])
def get_livros():
    parametros = request.args
    busca = parametros.get('busca', None)
    livro = dao_livro.get_livros(busca)
    return make_response(jsonify(livro))

@app_livro.route('/livros/<int:id>/', methods=['GET'])
def livro_id(id: int):
    livro = dao_livro.get_livros_by_id(id)
    if not livro:
        return Response({}, status=404)
    return make_response(jsonify(livro.get_json()))

@app_livro.route('/livros/autor/', methods=['GET'])
def get_livros_autor():
    parametros = request.args
    busca = parametros.get('busca', None)
    livros = dao_livro.get_livros_by_autor(busca)
    livros_by_autor = []
    for data in livros:
        livros_by_autor.append(data.get_json())
    return make_response(jsonify(livros_by_autor))

@app_livro.route('/livros/ano/', methods=['GET'])
def get_livros_ano():
    parametros = request.args
    busca = parametros.get('busca', None)
    livros = dao_livro.get_livros_by_ano(busca)
    livros_by_ano = []
    for data in livros:
        livros_by_ano.append(data.get_json())
    return make_response(jsonify(livros_by_ano))

@app_livro.route('/livros/<int:id>/', methods=['DELETE'])
def delete_livro(id: int):
    livro = dao_livro.get_livros_by_id(id)
    if livro:
        return Response(dao_livro.delete_livro(id), status=202)
    return Response({'Livro nao encontrado'}, status=404)

@app_livro.route('/livros/<int:id>/', methods=['PUT'])
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

