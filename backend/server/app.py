from flask import Flask

from edges import edges
from nodes import nodes
import config

app = Flask(__name__)
app.register_blueprint(edges)
app.register_blueprint(nodes)


if __name__ == '__main__':
    app.run(host=config.host, port=config.port)
