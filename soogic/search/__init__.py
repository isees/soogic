from flask import Blueprint

bp = Blueprint('search', __name__)


@bp.record_once
def register(state):
    from soogic.search import views
