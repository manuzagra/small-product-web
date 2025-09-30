from flask import Blueprint, render_template
import json

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    with open('data/products.json') as f:
        products = json.load(f)
    return render_template('index.html', products=products)


@bp.route('/product/<int:product_id>')
def product(product_id):
    with open('data/products.json') as f:
        products = json.load(f)
    product_obj = products[product_id] if 0 <= product_id < len(products) else None
    return render_template('product.html', product=product_obj) if product_obj else ('Product not found', 404)