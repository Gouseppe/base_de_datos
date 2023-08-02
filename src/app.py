from flask import Flask
from config import config

# Routes
from routes import Clientes
from routes import Pedidos

app = Flask(__name__)


def page_not_found(error):
    return "<h1>Error!! página no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    app.register_blueprint(Clientes.main, url_prefix='/customers')
    app.register_blueprint(Pedidos.main, url_prefix='/orders')

    app.register_error_handler(404, page_not_found)
    app.run()
