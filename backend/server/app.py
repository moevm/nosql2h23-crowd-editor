from flask import Flask
from flask_cors import CORS

from edges import edges
from nodes import nodes
import config

app = Flask(__name__)

CORS(app)

app.register_blueprint(edges)
app.register_blueprint(nodes)


if __name__ == '__main__':
    app.run(host=config.host, port=config.port)
