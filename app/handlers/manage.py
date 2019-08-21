from flask import request, jsonify, render_template, redirect

from app.models import Url, db


def index():
    urls = Url.query.all()
    
    return render_template(
        'index.html', title='Home', urls=urls
    )


def redirect_to_url(short_url):
    original_url = (
        Url.query.filter_by(short_url=short_url).first().original_url
    )
    return redirect(original_url)


def add_url(original_url):
    new_url = Url(original_url=original_url)
    db.session.add(new_url)
    db.session.commit()
    
    return jsonify({
        'new_url': new_url,
        'error': False,
    })


def register(app):
    app.add_url_rule('/', view_func=index)
    app.add_url_rule('/redirect_to_url', view_func=redirect_to_url)
    app.add_url_rule('/add_url/', view_func=add_url, methods=['POST'])
