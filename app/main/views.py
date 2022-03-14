
from flask import render_template , request, redirect, url_for
from . import main
from flask_wtf import FlaskForm
from .forms import BlogForm
from ..models import User,Blog
from .. import db
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user


@main.route('/')
def index():

    return render_template('index.html')



@main.route('/blog', methods=['GET', 'POST'])
@login_required
def blog():
    form = BlogForm()
    user = User

    if form.validate_on_submit():
        blog = Blog(owner_id=current_user.id, title=form.title.data,
                      category=form.category.data, content=form.content.data)
        form.title.data = ''
        form.category.data = ''
        form.content.data = ''

        db.session.add(blog)
        db.session.commit()
    return render_template('blog.html', form=form, user=user)






