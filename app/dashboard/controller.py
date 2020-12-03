from flask import Blueprint, request, render_template, redirect, url_for, session, flash
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from app.models import Customer, Category, Product, Order
from app.utils import login_required, customer_required
from app.account.forms import LoginForm, RegistrationForm, ForgotPassword
from app.dashboard.forms import CreateCategory, CreateProduct

mod_dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')


@mod_dashboard.route('/')
@login_required
def dashboard():
    return render_template("dashboard/dashboard.html", title="Dashboard")


@mod_dashboard.route('/category/overview')
@login_required
def category_overview():
    category_results = Category.query.all()
    categories = []
    for i in category_results:
        categories.append({
            'id': i.id,
            'name': i.name,
            'description': i.description
        })
    return render_template("dashboard/category/overview.html", title="Category Overview", categories=categories)


@mod_dashboard.route('/product/overview')
@login_required
def product_overview():
    product_results = Product.query.all()
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
    return render_template("dashboard/product/overview.html", title="Category Overview", products=products)


@mod_dashboard.route('/category/add', methods=['GET', 'POST'])
@login_required
def create_category():
    form = CreateCategory(request.form)
    if form.validate_on_submit():
        category = Category.query.filter_by(name=form.name.data).first()
        if not category:
            category = Category(name=form.name.data, description=form.description.data)
            db.session.add(category)
            db.session.commit()
            return redirect('/dashboard/category/overview')
        flash('User already exists', 'error-message')
    return render_template("dashboard/category/add.html", form=form, title="Create Category")


@mod_dashboard.route('/product/add', methods=['GET', 'POST'])
@login_required
def create_product():
    form = CreateProduct(request.form)
    if form.validate_on_submit():
        product = Product.query.filter_by(name=form.name.data).first()
        category = Category.query.filter_by(name=form.category_name.data).first()
        category_id = category.id
        if not product:
            product = Product(name=form.name.data, description=form.description.data,
                                    type=form.type.data, manufacturer=form.manufacturer.data,
                                    brand_name=form.brand_name.data, color=form.color.data,
                                    size=form.size.data, weight=form.weight.data,
                                    size_unit_measurement=form.size_unit_measurement.data,
                                    weight_unit_measurement=form.weight_unit_measurement.data,
                                    cost=form.cost.data, price=form.price.data, status=form.status.data,
                                    category_id=category_id, product_url=form.name.data)
            db.session.add(product)
            db.session.commit()
            return redirect('/dashboard/product/overview')
        flash('User already exists', 'error-message')
    return render_template("dashboard/product/add.html", form=form, title="Create Category")


@mod_dashboard.route('/category/remove/<category_id>', methods=['GET'])
@login_required
def remove_category(category_id):
    category = Category.query.filter_by(id=category_id).first()
    db.session.delete(category)
    db.session.commit()
    return redirect('/dashboard/category/overview')


@mod_dashboard.route('/product/remove/<product_id>', methods=['GET'])
@login_required
def remove_product(product_id):
    product = Product.query.filter_by(id=product_id).first()
    db.session.delete(product)
    db.session.commit()
    return redirect('/dashboard/product/overview')
