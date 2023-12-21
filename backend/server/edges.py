from flask import Blueprint, request, jsonify

from backend.dbms import dbms

edges = Blueprint('urls', __name__,)


@edges.route("/review/all", methods=["GET"])
def get_users():
    error, users = dbms.get_reviews()
    if not error:
        return jsonify(users), 200
    return error, 500


@edges.route("/critique/all", methods=["GET"])
def get_books():
    error, books = dbms.get_critiques()
    if not error:
        return jsonify(books), 200
    return error, 500


@edges.route("/edit/all", methods=["GET"])
def get_books():
    error, books = dbms.get_edits()
    if not error:
        return jsonify(books), 200
    return error, 500
