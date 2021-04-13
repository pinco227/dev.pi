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
    settings = mongo.db.settings.find_one(
        {"_id": ObjectId('606a3310d5c7c22eeee180f6')})
    links = list(mongo.db.links.find())
    return dict(settings=settings, links=links)


@app.route("/home")
@app.route('/')
@register_breadcrumb(app, '.', 'Home')
def home():
    skills = list(mongo.db.skills.find())
    education = list(mongo.db.education.find())
    experience = list(mongo.db.experience.find())
    testimonials = list(mongo.db.testimonials.find({"approved": True}))
    return render_template("landing.html", skills=skills, education=education, experience=experience, testimonials=testimonials)


@app.route('/write-testimonial', methods=["GET", "POST"])
@register_breadcrumb(app, '.write-testimonial', 'Write Testimonial')
def add_testimonial():
    if request.method == "POST":
        testimonial = {
            "author": request.form.get("name"),
            "role": request.form.get("role"),
            "text": request.form.get("text"),
            "approved": False
        }
        mongo.db.testimonials.insert_one(testimonial)
        flash("Thank you for your feedback!")
        return redirect(url_for("home"))

    return render_template("write-testimonial.html")


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


# ADMIN PANEL
@app.route('/admin')
def admin():
    if not session.get("user"):
        return redirect(url_for("login"))

    return render_template("admin/dashboard.html")


@app.route('/admin/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get("username").lower() == os.environ.get("ADMIN_USERNAME").lower() and request.form.get("password") == os.environ.get("ADMIN_PASSWORD"):
            session["user"] = request.form.get("username").lower()
            flash("Welcome, {}".format(request.form.get("username")))
            return redirect(url_for("admin"))
        else:
            # username doesn't exist
            flash("Incorrect Username")
            return redirect(url_for("login"))

    return render_template("admin/login.html")


@app.route("/admin/logout")
def logout():
    if session.get("user"):
        session.pop("user")

    flash("You have been logged out")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
