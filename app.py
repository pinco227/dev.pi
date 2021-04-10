import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, Markup)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from datetime import date
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# Initialize Flask-Breadcrumbs
Breadcrumbs(app=app)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.context_processor
def context_processor():
    """Inject settings variable to all templates

    Returns:
        dict: settings db collection
    """
    return dict(settings=mongo.db.settings.find_one(
        {"_id": ObjectId('606a3310d5c7c22eeee180f6')}))


@app.route("/home")
@app.route('/')
@register_breadcrumb(app, '.', 'Home')
def home():
    skills = list(mongo.db.skills.find())
    education = list(mongo.db.education.find())
    experience = list(mongo.db.experience.find())
    testimonials = list(mongo.db.testimonials.find())
    return render_template("landing.html", skills=skills, education=education, experience=experience, testimonials=testimonials)


@app.route('/portfolio')
@register_breadcrumb(app, '.portfolio', 'Portfolio')
def portfolio():
    projects = list(mongo.db.projects.find())
    return render_template("portfolio.html", projects=projects)


def view_project_dlc(*args, **kwargs):
    """Get project details from requested url args

    Returns:
        dict: text to be displayed into breadcrumb (Project title)
    """
    slug = request.view_args['project']
    project = mongo.db.projects.find_one({"slug": slug})
    return [{'text': project['title']}]


@app.route('/portfolio/<project>')
@register_breadcrumb(app, '.portfolio.project', '', dynamic_list_constructor=view_project_dlc)
def get_project(project):
    project = mongo.db.projects.find_one({"slug": project})
    return render_template("project.html", project=project)


@app.route('/blog')
@register_breadcrumb(app, '.blog', 'Blog')
def blog():
    blogs = list(mongo.db.blogs.find())
    # today = date.today().strftime("%B %d, %Y")
    return render_template("blog.html", blogs=blogs)


def view_blog_dlc(*args, **kwargs):
    """Get blg post details from requested url args

    Returns:
        dict: text to be displayed into breadcrumb (Blog title)
    """
    slug = request.view_args['post']
    post = mongo.db.blogs.find_one({"slug": slug})
    return [{'text': post['title']}]


@app.route('/blog/<post>')
@register_breadcrumb(app, '.blog.post', '', dynamic_list_constructor=view_blog_dlc)
def get_post(post):
    post = mongo.db.blogs.find_one({"slug": post})
    return render_template("blog-post.html", post=post)


@app.route('/contact')
@register_breadcrumb(app, '.contact', 'Contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
