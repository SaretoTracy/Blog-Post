from wtforms import StringField, PasswordField, BooleanField,  SelectField, TextAreaField, SubmitField
from flask_wtf import FlaskForm, form
from wtforms.validators import InputRequired, Email
from wtforms.widgets import TextArea

class BlogForm(FlaskForm):

    title = StringField('Title of Blog', validators=[InputRequired()])
    category = SelectField(u'Select Blog Category', choices=[('....Select Category', 'Select Category.....'), (
        'Fashion', 'Fashion'), ('Love', 'Love'), ('Home', 'Home'), ('Family', 'Family'), ('Beauty', 'Beauty'), ('Politics', 'Politics')])
    content = StringField(
        'Blog', validators=[InputRequired()], widget=TextArea())

class UpdateProfile(FlaskForm):
    fullname = StringField('FullName.',validators = [InputRequired()])
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')


