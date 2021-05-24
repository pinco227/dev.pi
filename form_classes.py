from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.recaptcha.validators import Recaptcha
from wtforms import StringField, TextAreaField, SubmitField, HiddenField
from wtforms.fields.html5 import EmailField, IntegerRangeField
from wtforms.validators import DataRequired, Email, NumberRange, URL, Optional


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


class UpdateTestimonials(FlaskForm):
    submit = SubmitField('Update')


class AddBlogForm(FlaskForm):
    title = StringField('Title', validators=[
        DataRequired(message="Please fill in Title field!")])
    slug = StringField('Slug', validators=[
                       DataRequired(message="Slug is required!")])
    url_for_files = HiddenField(id="url-for-files")
    collection = HiddenField()
    photo_list = HiddenField()
    body = TextAreaField('Text')
    submit = SubmitField('Add')


class EditBlogForm(FlaskForm):
    title = StringField('Title', validators=[
        DataRequired(message="Please fill in Title field!")])
    initial_slug = HiddenField()
    slug = StringField('Slug', validators=[
                       DataRequired(message="Slug is required!")])
    body = TextAreaField('Text')
    submit = SubmitField('Update')


class AddProjectForm(FlaskForm):
    title = StringField('Title', validators=[
        DataRequired(message="Please fill in Title field!")])
    slug = StringField('Slug', validators=[
                       DataRequired(message="Slug is required!")])
    tech = StringField('Technologies Used')
    repo = StringField('Source Code (repository URL)', validators=[Optional(),
                       URL(message="Invalid URL for Source Code!")])
    live_url = StringField('Live URL', validators=[Optional(),
                           URL(message="Invalid URL for Live Project!")])
    description = TextAreaField('Description')
    url_for_files = HiddenField(id="url-for-files")
    collection = HiddenField()
    photo_list = HiddenField()
    submit = SubmitField('Add')


class EditProjectForm(FlaskForm):
    title = StringField('Title', validators=[
        DataRequired(message="Please fill in Title field!")])
    initial_slug = HiddenField()
    slug = StringField('Slug', validators=[
                       DataRequired(message="Slug is required!")])
    tech = StringField('Technologies Used')
    repo = StringField('Source Code (repository URL)', validators=[Optional(),
                       URL(message="Invalid URL for Source Code!")])
    live_url = StringField('Live URL', validators=[Optional(),
                           URL(message="Invalid URL for Live Project!")])
    description = TextAreaField('Description')
    submit = SubmitField('Update')


class AddSkillForm(FlaskForm):
    name = StringField('Skill name', validators=[
        DataRequired(message="Please fill in the Skill name!")])
    percentage = IntegerRangeField(
        'Percentage', default=50, validators=[NumberRange(min=0, max=100, message='Percentage should be between 0 and 100!')])
    submit = SubmitField('Add')


class UpdateSkills(FlaskForm):
    submit = SubmitField('Update')
