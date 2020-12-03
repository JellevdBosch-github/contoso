from flask import Blueprint, request, render_template, redirect, url_for, session, flash
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from app.models import Customer
from app.utils import login_required
from app.account.forms import LoginForm, RegistrationForm, ForgotPassword

mod_account = Blueprint('account', __name__, url_prefix='/account')


@mod_account.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm(request.form)
    # if request.method == "POST":
    #     form.date_of_birth.data = form.date_of_birth.raw_data[0]
    #     print(form.date_of_birth.data)
    if form.validate_on_submit():
        user = Customer.query.filter_by(email=form.email.data).first()
        if not user:
            customer = Customer(first_name=form.first_name.data, middle_name=form.middle_name.data,
                                last_name=form.last_name.data, gender=form.gender.data, title=form.title.data,
                                birth_date=form.date_of_birth.raw_data[0], phone_number=form.phone_number.data,
                                country=form.country.data, city=form.city.data, street=form.street.data,
                                zip_code=form.postal_code.data, house_number=form.house_number.data,
                                email=form.email.data, password=form.password.data)
            db.session.add(customer)
            db.session.commit()
            session['user'] = {
                'id': customer.id,
                'first_name': customer.first_name,
                'middle_name': customer.middle_name,
                'last_name': customer.last_name,
                'title': customer.title,
                'birth_date': customer.birth_date,
                'phone_number': customer.phone_number,
                'country': customer.country,
                'city': customer.city,
                'street': customer.street,
                'zip_code': customer.zip_code,
                'house_number': customer.house_number,
                'email': customer.email,
            }
            session['logged_in'] = True
            return redirect('/')
        flash('User already exists', 'error-message')
    return render_template("account/signup.html", form=form, title="Sign up")


@mod_account.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        customer = Customer.query.filter_by(email=form.email.data, password=form.password.data).first()
        if customer:
            session['user'] = {
                'id': customer.id,
                'first_name': customer.first_name,
                'middle_name': customer.middle_name,
                'last_name': customer.last_name,
                'title': customer.title,
                'birth_date': customer.birth_date,
                'phone_number': customer.phone_number,
                'country': customer.country,
                'city': customer.city,
                'street': customer.street,
                'zip_code': customer.zip_code,
                'house_number': customer.house_number,
                'email': customer.email,
            }
            session['logged_in'] = True
            next_page = request.args.get("next")
            if next_page:
                return redirect(next_page)
            else:
                return redirect('/')
        flash('Unknown combination of email and password!', 'error-message')
    return render_template("account/signin.html", form=form, title="Sign in")


@mod_account.route('/signout', methods=['GET', 'POST'])
@login_required
def signout():
    session.pop('logged_in')
    session.pop('user')
    return redirect('/')


@mod_account.route('/forgot_password', methods=['GET', 'POST'])
def forgot():
    pass


@mod_account.route('/confirm_registration', methods=['GET', 'POST'])
def confirm():
    pass


@mod_account.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    pass
