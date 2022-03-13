from flask import Blueprint
from flask import render_template,request
from . import auth

auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
     # getting info from form
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #form validation
        if len(email) < 4:
            flash('Email is too short')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.')
        elif password1 != password2:
            flash('Passwords don\'t match')
        elif len(password1) < 6:
            flash('Password must be at least 6 characters.')
    return render_template('signup.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')