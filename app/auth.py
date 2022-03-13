from flask import Blueprint
from flask import render_template,request,flash
from . import auth

auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
     # getting info from form
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #form validation
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('username must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Account created successfully', category='success')
    return render_template('signup.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')