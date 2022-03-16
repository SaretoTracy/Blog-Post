
from flask import render_template , request, redirect, url_for
from . import main

from flask_wtf import FlaskForm
from .forms import BlogForm,UpdateProfile,UpdateBlog
from ..models import User,Blog
from .. import db,photos
from ..email import mail_message
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user


@main.route('/',methods = ["GET","POST"])
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

@main.route('/user/<uname>')
@login_required
def profile(uname):

    blog = Blog.query.filter_by(id=current_user.id).all()
    user = User.query.filter_by(username=uname).first()

    return render_template('profile/profile.html', name=current_user.username, email=current_user.email, password=current_user.password, user=user, blog=blog)

@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        return redirect(url_for('.error'))

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))


# @main.route('/user/<uname>/updateblog', methods=['GET', 'POST'])
# @login_required
# def updateblog(uname):
#     user = User.query.filter_by(username=uname).first()
#     if user is None:
#         return redirect(url_for('.error'))

#     form = UpdateBlog()
#     if form.validate_on_submit():
#         content = form.content.data

#         blog = Blog(user)
#         db.session.add(blog)
#         db.session.commit()

#         return redirect(url_for('auth.dashboard', uname=user.username))

#     return render_template('blogpost/updateblog.html', form=form)






