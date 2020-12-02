from flask import Blueprint, request, render_template, redirect, url_for, session, flash
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from app.models import Customer
from app.utils import login_required
from app.account.forms import LoginForm, RegistrationForm, ForgotPassword

mod_store = Blueprint('store', __name__, url_prefix='/')


@mod_store.route('/')
def store():
    # TODO categories ophalen en doorsturen
    categories = [{
        'id': 1,
        'name': 'Category Name Test',
        'description': 'Category Description Test '
    }]
    return render_template("store/store.html", title="Store", categories=categories)


@mod_store.route('/categories')
def categories():
    # TODO categories ophalen en doorsturen
    categories = [{
        'id': 1,
        'name': 'Category Name Test',
        'description': 'Category Description Test '
    }]
    return render_template("store/categories.html", title="Store Categories", categories=categories)


@mod_store.route('/category/<category_name>', methods=['GET', 'POST'])
def category(category_name):
    # TODO products ophalen en doorsturen
    products = [
        {
            'id': 1,
            'name': 'Product Name Test',
            'description': 'Product Description Test',
            'price': 10.99
        },
        {
            'id': 2,
            'name': 'Product Name Test2',
            'description': 'Product Description Test2',
            'price': 11.99
        },
        {
            'id': 3,
            'name': 'Product Name Test3',
            'description': 'Product Description Test2',
            'price': 11.99
        },
        {
            'id': 4,
            'name': 'Product Name Test4',
            'description': 'Product Description Test2',
            'price': 11.99
        }
    ]
    brands = ['Nike', 'BMW', 'Samsung']
    statuses = ['Available', 'Unavailable']
    return render_template("store/category.html", title=category_name, products=products, brands=brands, statuses=statuses,
                           category=category_name, result_amount=len(products))


@mod_store.route('/product/<product_id>/<product_name>')
def product(product_id, product_name):
    # TODO product ophalen en doorsturen
    product = {
        'id': 1,
        'name': 'Product Name Test',
        'description': 'Product Description Test',
        'price': 11.99,
        'status': 'Available'
    }
    return render_template("store/product.html", title=product_name, product=product)


@mod_store.route('/buy/<product_id>/<product_name>')
@login_required
def checkout(product_id, product_name):
    # TODO product ophalen en doorsturen
    product = {
        'id': 4,
        'name': 'Product Name Test4',
        'description': 'Product Description Test2',
        'price': 11.99,
        'status': 'Available'
    }
    return render_template("store/checkout.html", title="Checkout", product=product)
