
from flask import render_template
from . import main


@main.route('/')
def index():

    return render_template('index.html')

@main.route('/signup')
def signup():

    return render_template('signup.html')



