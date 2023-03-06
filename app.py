from flask import Flask
from database.connect import ConnectDataBase
from modulos.livro.controller_livro import app_livro
from modulos.cliente.controller_cliente import app_cliente
from modulos.aluguel.controller_aluguel import app_aluguel


app = Flask(__name__)
ConnectDataBase().init_table()

app.register_blueprint(app_livro)
app.register_blueprint(app_cliente)
app.register_blueprint(app_aluguel)


if __name__ == '__main__':
    app.run(debug=True)