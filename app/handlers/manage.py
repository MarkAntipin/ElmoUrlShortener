from flask import request, jsonify


def index():
    result = 0
    return jsonify({
        'result': result,
        'error': False,
    })


def register(app):
    app.add_url_rule('/', view_func=index)
