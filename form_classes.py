from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, NumberRange, URL


class WriteTestimonialForm(FlaskForm):
    name = StringField('Your Name', validators=[
                       DataRequired(message="Please fill in your name!")])
    role = StringField('[Role name] at [Company name]', validators=[
                       DataRequired(message="Please fill in your role!")])
    text = StringField('Your message', validators=[
                       DataRequired(message="Please type your message!")])
