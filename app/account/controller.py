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
    if form.validate_on_submit():
        user = Customer.query.filter_by(email=form.email.data).first()
        if not user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            session['logged_in'] = True
            return redirect('/')
        flash('User already exists', 'error-message')
    return render_template("account/signup.html", form=form, title="Sign in")


@mod_account.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = Customer.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
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
    pass


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
