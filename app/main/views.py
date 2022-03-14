
from flask import render_template
from . import main
from .forms import BlogForm
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
        blog = blog(owner_id=current_user.id, title=form.title.data,
                      category=form.category.data, content=form.content.data)
        form.title.data = ''
        form.category.data = ''
        form.content.data = ''

        db.session.add(blog)
        db.session.commit()
    return render_template('blog.html', form=form, user=user)






