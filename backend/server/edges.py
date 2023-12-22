from flask import Blueprint, request, jsonify

from dbms import dbms

edges = Blueprint('edges', __name__,)


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
def get_propositions():
    error, propositions = dbms.get_propositions()
    if not error:
        return jsonify(propositions), 200
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


@edges.route("/proposition", methods=["GET"])
def get_proposition():
    filter_data = request.json
    error, propositions = dbms.filter_propositions(filter_data)
    if not error:
        return jsonify(propositions), 200
    return error, 500


# edit
@edges.route("/review/edit", methods=["POST"])
def edit_review():
    edit_data = request.json
    error, reviews = dbms.edit_review(edit_data)
    if not error:
        return jsonify(reviews), 200
    return error, 500


@edges.route("/critique/edit", methods=["POST"])
def edit_critique():
    edit_data = request.json
    error, critiques = dbms.edit_critique(edit_data)
    if not error:
        return jsonify(critiques), 200
    return error, 500


@edges.route("/proposition/edit", methods=["POST"])
def edit_proposition():
    edit_data = request.json
    error, propositions = dbms.edit_proposition(edit_data)
    if not error:
        return jsonify(propositions), 200
    return error, 500


# add
@edges.route("/review/add", methods=["POST"])
def add_review():
    add_data = request.json
    error, reviews = dbms.add_book_review(add_data)
    if not error:
        return jsonify(reviews), 200
    return error, 500


@edges.route("/critique/add", methods=["POST"])
def add_critique():
    add_data = request.json
    error, critiques = dbms.add_critique(add_data)
    if not error:
        return jsonify(critiques), 200
    return error, 500


@edges.route("/proposition/add", methods=["POST"])
def add_proposition():
    add_data = request.json
    error, propositions = dbms.add_proposition(add_data)
    if not error:
        return jsonify(propositions), 200
    return error, 500


# delete
@edges.route("/review/delete", methods=["DELETE"])
def delete_review():
    delete_data = request.json
    error, users = dbms.delete_review(delete_data)
    if error:
        return error, 500
    return 200


@edges.route("/critique/delete", methods=["DELETE"])
def delete_critique():
    delete_data = request.json
    error, users = dbms.delete_critique(delete_data)
    if error:
        return error, 500
    return 200


@edges.route("/proposition/delete", methods=["DELETE"])
def delete_proposition():
    delete_data = request.json
    error, users = dbms.delete_proposition(delete_data)
    if error:
        return error, 500
    return 200
