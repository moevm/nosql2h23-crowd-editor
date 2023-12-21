from flask import Blueprint, request, jsonify

from backend.dbms import dbms

nodes = Blueprint('urls', __name__,)


@nodes.route("/users/all", methods=["GET"])
def get_users():
    error, users = dbms.get_users()
    if not error:
        return jsonify(users), 200
    return error, 500


@nodes.route("/books/all", methods=["GET"])
def get_books():
    error, books = dbms.get_books()
    if not error:
        return jsonify(books), 200
    return error, 500


@nodes.route("/user", methods=["GET"])
def get_user():
    filter_data = request.json
    error, users = dbms.filter_users(filter_data)
    if not error:
        return jsonify(users), 200
    return error, 500


@nodes.route("/book", methods=["GET"])
def get_book():
    filter_data = request.json
    error, books = dbms.filter_books(filter_data)
    if not error:
        return jsonify(books), 200
    return error, 500


@nodes.route("/user/edit", methods=["POST"])
def edit_user():
    edit_data = request.json
    error = dbms.edit_user(edit_data)
    if error:
        return error, 500
    return 200


@nodes.route("/book/edit", methods=["POST"])
def edit_book():
    edit_data = request.json
    error = dbms.edit_book(edit_data)
    if error:
        return error, 500
    return 200


@nodes.route("/user/add", methods=["POST"])
def add_user():
    add_data = request.json
    error, users = dbms.add_user(add_data)
    if error:
        return error, 500
    return 200


@nodes.route("/book/add", methods=["POST"])
def add_book():
    add_data = request.json
    error, users = dbms.add_book(add_data)
    if error:
        return error, 500
    return 200
