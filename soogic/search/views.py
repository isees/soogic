from flask import render_template
from soogic import db
from soogic.search import bp
from soogic.search.models import Product


@bp.route('/', methods=['GET'])
def index():
    return render_template('/wx/search/index.html')


@bp.route('/detail/<string:model>', methods=['GET'])
def detail(model=None):
    items = Product.query.filter(Product.fitting_model == model).first() if model is not None else None
    return render_template('/wx/search/detail.html', items=items)
