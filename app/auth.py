from flask import Blueprint
from flask import render_template
from . import auth

auth = Blueprint('auth', __name__)


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/login')
def login():
    return render_template('login.html')