from flask import (
    render_template, redirect
)

from app.models import Url, db
from app.forms import UrlForm


def base():
    return redirect('add_url')


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


def add_url():
    form = UrlForm()
    if form.validate_on_submit():
        url = Url(original_url=form.original_url.data)
        db.session.add(url)
        db.session.commit()
        return redirect('/index')
    return render_template('add_url.html', title='Add Url', form=form)


def register(app):
    app.add_url_rule('/', view_func=base)
    app.add_url_rule('/index', view_func=index)
    app.add_url_rule('/<short_url>', view_func=redirect_to_url)
    app.add_url_rule('/add_url', view_func=add_url, methods=['GET', 'POST'])
