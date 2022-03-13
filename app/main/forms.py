from wtforms import StringField, PasswordField, BooleanField
from flask_wtf import FlaskForm, form
from wtforms.validators import InputRequired, Email
from wtforms.widgets import TextArea

class BlogForm(FlaskForm):

    title = StringField('Title of Blog', validators=[InputRequired()])
    category = SelectField(u'Select Blog Category', choices=[('....Select Category', 'Select Category.....'), (
        'Fashion', 'Fashion'), ('Love', 'Love'), ('Home', 'Home'), ('Family', 'Family'), ('Beauty', 'Beauty'), ('Politics', 'Politics')])
    description = StringField(
        'Blog', validators=[InputRequired()], widget=TextArea())

