import logging
import sys
import pkg_resources
from flask import Flask
from flask import render_template, url_for, redirect
from flask_alembic import Alembic
from flask_alembic.cli.click import cli as alembic_cli
from flask_babel import Babel
# from sopy.ext.sqlalchemy import SQLAlchemy


__version__ = pkg_resources.get_distribution('soogic').version

alembic = Alembic()
babel = Babel()
db = SQLAlchemy()