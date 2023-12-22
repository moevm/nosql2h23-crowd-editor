from flask import Flask, request, jsonify

from backend.dbms import dbms
from backend.server import config

app = Flask(__name__)

@app.route("/users/all", methods=["GET"])
def get_users_all():
    error, users = dbms.get_users()
    if not error:
        return jsonify(users), 200
    return error, 500


@app.route("/books/all", methods=["GET"])
def get_books_all():
    error, books = dbms.get_books()
    if not error:
        return jsonify(books), 200
    return error, 500


@app.route("/user", methods=["GET"])
def get_users():
    filter_data = request.json
    error, users = dbms.filter_users(filter_data)
    if not error:
        return jsonify(users), 200
    return error, 500


@app.routes("/book", methods=["GET"])
def get_book():
    filter_data = request.json
    error, books = dbms.filter_books(filter_data)
    if not error:
        return jsonify(books), 200
    return error, 500


@app.route("/user/edit", methods=["POST"])
def edit_user():
    edit_data = request.json
    check = dbms.edit_user(edit_data)
    if check:
        return 200
    return 500


@app.route("/book/edit", methods=["POST"])
def edit_book():
    edit_data = request.json
    check = dbms.edit_book(edit_data)
    if check:
        return 200
    return 500


@app.route("/user/add", methods=["POST"])
def add_user():
    add_data = request.json
    error_msg, users = dbms.add_user(add_data)
    if not error_msg:
        return 200
    return 500


@app.route("/book/add", methods=["POST"])
def add_book():
    add_data = request.json
    error_msg, books = dbms.add_book(add_data)
    if error_msg:
        return 200
    return 500


if __name__ == '__main__':
    app.run(host=config.host, port=config.port)
