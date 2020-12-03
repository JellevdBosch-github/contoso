from flask import Blueprint, request, render_template, redirect, url_for, session, flash
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from app.models import Customer, Category, Product, Order
from app.utils import login_required, customer_required
from app.account.forms import LoginForm, RegistrationForm, ForgotPassword

mod_store = Blueprint('store', __name__, url_prefix='/')


@mod_store.route('/')
def store():
    category_results = Category.query.limit(5)
    categories = []
    for i in category_results:
        categories.append({
            'id': i.id,
            'name': i.name,
            'description': i.description
        })
    return render_template("store/store.html", title="Store", categories=categories)


@mod_store.route('/categories')
def categories():
    category_results = Category.query.all()
    categories = []
    for i in category_results:
        categories.append({
            'id': i.id,
            'name': i.name,
            'description': i.description
        })
    return render_template("store/categories.html", title="Store Categories", categories=categories)


@mod_store.route('/category/<category_id>/<category_name>', methods=['GET', 'POST'])
def category(category_id, category_name):
    if request.args:
        min = request.args.get('min_amount')
        max = request.args.get('max_amount')
        product_results = Product.query.filter_by(category_id=category_id).filter(Product.price >= min, Product.price <= max).all()
    else:
        product_results = Product.query.filter_by(category_id=category_id).all()
    products = []
    for i in product_results:
        products.append({
            'id': i.id,
            'name': i.name,
            'description': i.description,
            'weight': i.weight,
            'weight_unit': i.weight_unit_measurement,
            'size': i.size,
            'size_unit': i.size_unit_measurement,
            'color': i.color,
            'status': i.status,
            'type': i.type,
            'price': i.price,
            'manufacturer': i.manufacturer,
            'brand_name': i.brand_name
        })
    max_cost = 0
    for i in products:
        if i['price'] > max_cost:
            max_cost = i['price']
    return render_template("store/category.html", title=category_name, products=products,
                           category=category_name, result_amount=len(products), max_cost=max_cost)


@mod_store.route('/product/<product_id>/<product_name>')
def product(product_id, product_name):
    i = Product.query.filter_by(id=product_id).first()
    product = {
        'id': i.id,
        'name': i.name,
        'description': i.description,
        'weight': i.weight,
        'weight_unit': i.weight_unit_measurement,
        'size': i.size,
        'size_unit': i.size_unit_measurement,
        'color': i.color,
        'status': i.status,
        'type': i.type,
        'price': i.price,
        'manufacturer': i.manufacturer,
        'brand_name': i.brand_name
    }
    return render_template("store/product.html", title=product_name, product=product)


@mod_store.route('/buy/<product_id>/<product_name>', methods=['GET', 'POST'])
@login_required
@customer_required
def checkout(product_id, product_name):
    i = Product.query.filter_by(id=product_id).first()
    product = {
        'id': i.id,
        'name': i.name,
        'description': i.description,
        'weight': i.weight,
        'weight_unit': i.weight_unit_measurement,
        'size': i.size,
        'size_unit': i.size_unit_measurement,
        'color': i.color,
        'status': i.status,
        'type': i.type,
        'price': i.price,
        'manufacturer': i.manufacturer,
        'brand_name': i.brand_name
    }
    if request.method == 'POST':
        order = Order(customer_id=session['user']['id'], product_id=product_id, cost=product['price'])
        db.session.add(order)
        db.session.commit()
        return redirect('/')
    else:
        return render_template("store/checkout.html", user=session['user'], title="Checkout", product=product)
