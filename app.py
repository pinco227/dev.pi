import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, Markup)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

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
def home():
    skills = list(mongo.db.skills.find())
    education = list(mongo.db.education.find())
    experience = list(mongo.db.experience.find())
    testimonials = list(mongo.db.testimonials.find())
    return render_template("landing.html", skills=skills, education=education, experience=experience, testimonials=testimonials)


@app.route('/portfolio')
def portfolio():
    projects = list(mongo.db.projects.find())
    return render_template("portfolio.html", projects=projects)


@app.route('/portfolio/<project>')
def get_project(project):
    project = mongo.db.projects.find_one({"slug": project})
    return render_template("project.html", project=project)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
