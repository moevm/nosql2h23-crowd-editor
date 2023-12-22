from flask import Blueprint, request, jsonify
import json

from dbms import dbms

nodes = Blueprint('nodes', __name__,)


# get all
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


# filter
@nodes.route("/user", methods=["GET"])
def get_user():
    filter_param = request.args.get('filter')
    get_param = request.args.get('get')
    try:
        filter_json = json.loads(filter_param) if filter_param else None
        get_json = json.loads(get_param) if get_param else None
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format"}), 400

    filter_data = {"filter": filter_json, "get": get_json}
    print(filter_data)
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


# edit
@nodes.route("/user/edit", methods=["POST"])
def edit_user():
    edit_data = request.json
    error = dbms.edit_user(edit_data)
    if error:
        return error, 500
    return {"success": True}, 200


@nodes.route("/book/edit", methods=["POST"])
def edit_book():
    edit_data = request.json
    error = dbms.edit_book(edit_data)
    if error:
        return error, 500
    return {"success": True}, 200


# add
@nodes.route("/user/add", methods=["POST"])
def add_user():
    add_data = request.json
    error = dbms.add_user(add_data)
    if error:
        return error, 500
    return {"success": True}, 200


@nodes.route("/book/add", methods=["POST"])
def add_book():
    add_data = request.json
    error, users = dbms.add_book(add_data)
    if error:
        return error, 500
    return {"success": True}, 200


# delete
@nodes.route("/user/delete", methods=["DELETE"])
def delete_user():
    delete_data = request.json
    error, users = dbms.delete_user(delete_data)
    if error:
        return error, 500
    return {"success": True}, 200


@nodes.route("/book/delete", methods=["DELETE"])
def delete_book():
    delete_data = request.json
    error, users = dbms.delete_book(delete_data)
    if error:
        return error, 500
    return {"success": True}, 200
