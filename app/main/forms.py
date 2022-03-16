from wtforms import StringField, PasswordField, BooleanField,  SelectField, TextAreaField, SubmitField
from flask_wtf import FlaskForm, form
import email_validator
from ..models import User
from wtforms.validators import InputRequired, Email
from wtforms.widgets import TextArea

class BlogForm(FlaskForm):

    title = StringField('Title of Blog', validators=[InputRequired()])
    category = SelectField(u'Select Blog Category', choices=[('....Select Category', 'Select Category.....'), (
        'Fashion', 'Fashion'), ('Love', 'Love'), ('Home', 'Home'),('Technology', 'Technology'), ('Family', 'Family'), ('Beauty', 'Beauty'), ('Politics', 'Politics')])
    content = StringField(
        'Blog', validators=[InputRequired()], widget=TextArea())

class UpdateProfile(FlaskForm):
    fullname = StringField('FullName.',validators = [InputRequired()])
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')


class SubscribedUserForm(FlaskForm):
    email = StringField('Enter Email Address to subscribe to our daily Updates',validators=[InputRequired(),Email()])
    submit = SubmitField('Subscribe')

    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('Email Already subscribed')




