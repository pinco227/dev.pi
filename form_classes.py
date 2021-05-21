from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.recaptcha.validators import Recaptcha
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, NumberRange, URL


class WriteTestimonialForm(FlaskForm):
    name = StringField('Your Name', validators=[
                       DataRequired(message="Please fill in your name!")])
    role = StringField('[Role name] at [Company name]', validators=[
                       DataRequired(message="Please fill in your role!")])
    text = TextAreaField('Your message', validators=[
        DataRequired(message="Please type your message!")])
    recaptcha = RecaptchaField(
        validators=[Recaptcha(message="Please check the security Recaptcha field!")])
    submit = SubmitField('Submit')


class ContactForm(FlaskForm):
    name = StringField('Your Name', validators=[
                       DataRequired(message="Please fill in your name!")])
    email = EmailField('Email Address', validators=[
        DataRequired(message="Please fill in your email address!"),
        Email(message="Invalid email address!")])
    subject = StringField('Subject', validators=[
        DataRequired(message="Please type a subject!")])
    message = TextAreaField('Your Message', validators=[
        DataRequired(message="Please type a message!")])
    recaptcha = RecaptchaField(
        validators=[Recaptcha(message="Please check the security Recaptcha field!")])
    submit = SubmitField('Send')
