from . import auth
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Blog,Comment,Quote
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from app.request import get_random_quote
from flask_login import login_user, current_user


from flask_wtf import FlaskForm
from .main.forms import BlogForm


from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():

    # getting info from form
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')

        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(username) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:

            new_user = User(email=email, username=username, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
    
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('auth.dashboard'))

    return render_template("signup.html", user=current_user)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('auth.dashboard'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)



@auth.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():

    
    quotes = get_random_quote()
    

    
    return render_template('dashboard.html', quotes=quotes)
@auth.route('/blogpost', methods=['GET', 'POST'])
@login_required
def blogpost():

    
    comment = Comment.query.all()
    print(comment)
    blog = Blog.query.all()
    
    

    
    return render_template('blogpost.html',blog=blog,comment=comment)

@auth.route("/create-comment/<blog_id>", methods=['POST'])
@login_required
def create_comment(blog_id):

    if request.method == 'POST':
        remark = request.form.get('remark')

    if not remark:
        flash('Comment cannot be empty.', category='error')
    else:
        blog = Blog.query.filter_by(id=blog_id)
        if blog:
            comment = Comment(
                remark=remark, owner_id=current_user.id, blog_id=blog_id)
            db.session.add(comment)
            db.session.commit()
        else:
            flash('blog does not exist.', category='error')

    return redirect(url_for('auth.blogpost'))

@auth.route("/delete-comment/<comment_id>")
@login_required
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()

    if not comment:
        flash('Comment does not exist.', category='error')
    elif current_user.id != comment.owner_id and current_user.id != comment.blog.owner_id:
        flash('You do not have permission to delete this comment.', category='error')
    else:
        db.session.delete(comment)
        db.session.commit()

    return redirect(url_for('auth.blogpost'))
@auth.route("/delete-blog/<id>")
@login_required
def delete_blog(id):
    blog = Blog.query.filter_by(id=id).first()

    if not blog:
        flash("blog does not exist.", category='error')
    elif current_user.id != blog.owner_id:
        flash('You do not have permission to delete this blog.', category='error')
    else:
        db.session.delete(blog)
        db.session.commit()
        flash('blog deleted.', category='success')

    return redirect(url_for('auth.blogpost'))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

