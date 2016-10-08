import logging
import sys
import pkg_resources
from flask import Flask
from flask import render_template, url_for, redirect
from flask_alembic import Alembic
from flask_alembic.cli.click import cli as alembic_cli
from flask_babel import Babel
from soogic.ext.SGSQLAlchemy import SGSQLAlchemy

__version__ = pkg_resources.get_distribution('soogic').version

alembic = Alembic()
babel = Babel()
db = SGSQLAlchemy()


def create_app(info=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('soogic.config')
    # app.config.from_pyfile('config.py', True)
    app.cli.add_command(alembic_cli, 'db')

    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    alembic.init_app(app)
    babel.init_app(app)
    db.init_app(app)

    from soogic.ext import views
    views.init_app(app)

    from soogic import search
    app.register_blueprint(search.bp, url_prefix='/search')
    # print app.__dict__

    @app.route('/')
    def index():
        # print 'what\'s going on?'
        return render_template('index.html')

    app.add_url_rule('/favicon.ico', None, app.send_static_file, defaults={'filename': 'favicon.ico'})
    app.add_url_rule('/robots.txt', None, app.send_static_file, defaults={'filename': 'robots.txt'})

    @app.errorhandler(403)
    def forbidden(e):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500

    if not app.debug:
        handler = logging.StreamHandler(sys.stderr)
        handler.setLevel(logging.ERROR)
        app.logger.addHandler(handler)

    return app
