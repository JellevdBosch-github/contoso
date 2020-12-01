from flask import Blueprint, request, render_template, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import db
from app.models import Customer

mod_account = Blueprint('account', __name__, url_prefix='/account')


@mod_account.route('/signup', methods=['GET', 'POST'])
def signup():
    pass


@mod_account.route('/signin', methods=['GET', 'POST'])
def signin():
    pass


@mod_account.route('/signout', methods=['GET', 'POST'])
def signout():
    pass


@mod_account.route('/forgot_password', methods=['GET', 'POST'])
def forgot():
    pass


@mod_account.route('/confirm_registration', methods=['GET', 'POST'])
def confirm():
    pass


@mod_account.route('/profile', methods=['GET', 'POST'])
def profile():
    pass
