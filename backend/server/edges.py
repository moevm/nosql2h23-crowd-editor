from flask import Blueprint, request, jsonify

from backend.dbms import dbms

edges = Blueprint('urls', __name__,)


# get all
@edges.route("/review/all", methods=["GET"])
def get_reviews():
    error, reviews = dbms.get_reviews()
    if not error:
        return jsonify(reviews), 200
    return error, 500


@edges.route("/critique/all", methods=["GET"])
def get_critiques():
    error, critiques = dbms.get_critiques()
    if not error:
        return jsonify(critiques), 200
    return error, 500


@edges.route("/edit/all", methods=["GET"])
def get_edits():
    error, edits = dbms.get_edits()
    if not error:
        return jsonify(edits), 200
    return error, 500


# filter
@edges.route("/review", methods=["GET"])
def get_review():
    filter_data = request.json
    error, reviews = dbms.filter_reviews(filter_data)
    if not error:
        return jsonify(reviews), 200
    return error, 500


@edges.route("/critique", methods=["GET"])
def get_critique():
    filter_data = request.json
    error, critiques = dbms.filter_critiques(filter_data)
    if not error:
        return jsonify(critiques), 200
    return error, 500


@edges.route("/edit", methods=["GET"])
def get_edit():
    filter_data = request.json
    error, edits = dbms.filter_edits(filter_data)
    if not error:
        return jsonify(edits), 200
    return error, 500


# edit
@edges.route("/review", methods=["POST"])
def edit_review():
    edit_data = request.json
    error, reviews = dbms.edit_review(edit_data)
    if not error:
        return jsonify(reviews), 200
    return error, 500


@edges.route("/critique", methods=["POST"])
def edit_critique():
    edit_data = request.json
    error, critiques = dbms.edit_critique(edit_data)
    if not error:
        return jsonify(critiques), 200
    return error, 500


@edges.route("/edit", methods=["POST"])
def edit_edit():
    edit_data = request.json
    error, edits = dbms.edit_edit(edit_data)
    if not error:
        return jsonify(edits), 200
    return error, 500


# add
@edges.route("/review", methods=["POST"])
def add_review():
    add_data = request.json
    error, reviews = dbms.add_review(add_data)
    if not error:
        return jsonify(reviews), 200
    return error, 500


@edges.route("/critique", methods=["POST"])
def add_critique():
    add_data = request.json
    error, critiques = dbms.add_critique(add_data)
    if not error:
        return jsonify(critiques), 200
    return error, 500


@edges.route("/edit", methods=["POST"])
def add_edit():
    add_data = request.json
    error, edits = dbms.add_edit(add_data)
    if not error:
        return jsonify(edits), 200
    return error, 500
