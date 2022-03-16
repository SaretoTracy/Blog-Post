from . import db
from flask_login import UserMixin
from . import login_manager
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash


# a model to define our user data.


# connect our class to our database and allow communication.

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    blogs = db.relationship('Blog', backref='owner')
    comments = db.relationship('Comment',backref='owner')



    def __repr__(self):
        return f"User('{self.username}')"


class Blog(db.Model):
    '''
    '''
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.String(), index=True)
    title = db.Column(db.String())
    category = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    comments = db.relationship('Comment',backref = 'blogs')

    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'Blog {self.content}'

class Comment(db.Model):
    _tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    remark = db.Column(db.String(255), index=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    blog_id = db.Column(db.Integer, db.ForeignKey("blogs.id"))
    

    def __repr__(self):
        return f'Comment {self.remark}'


class Quote:
    def __init__(self,author,quote):
        self.author = author
        self.quote = quote

    def __repr__(self):
        return f'Comment {self.quote}'
