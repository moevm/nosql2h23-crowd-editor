from flask import Flask, jsonify

from backend.dbms import dbms
from backend.server import config

app = Flask(__name__)


@app.route("/users/all", methods=["GET"])
def get_users():
    error, users = dbms.get_users()
    if not error:
        return jsonify(users), 200
    return error, 500


@app.route("/books/all", methods=["GET"])
def get_books():
    error, books = dbms.get_books()
    if not error:
        return jsonify(books), 200
    return error, 500


if __name__ == '__main__':
    app.run(host=config.host, port=config.port)
