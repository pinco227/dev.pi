import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, Markup, send_from_directory)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
from functools import wraps
from datetime import date
import random

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

# Initialize Flask-Breadcrumbs
Breadcrumbs(app=app)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config['UPLOAD_PATH'] = 'uploads'
app.config['UPLOAD_EXTENSIONS'] = [
    '.txt', '.doc', '.docx', '.pdf', '.png', '.jpg', '.jpeg', '.gif']
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024

mongo = PyMongo(app)


@app.context_processor
def context_processor():
    """Inject settings and links variables to all templates

    Returns:
        dict: settings and links db collections
    """
    settings = mongo.db.settings.find_one(
        {"_id": ObjectId('606a3310d5c7c22eeee180f6')})
    links = list(mongo.db.links.find())
    return dict(settings=settings, links=links)


@app.errorhandler(413)
def too_large(e):
    flash(Markup('''<strong>Sorry!</strong> File is to large. <br>
            <small>use <a href="https://tinypng.com/" target="_blank">TinyPNG</a> to compress and/or
            <a href="https://photoshop.adobe.com/resize" target="_blank">Photoshop Express</a> to resize.</small>'''))
    return redirect('/admin/' + request.url.split("/").pop()), 413


@app.route('/uploads/<filename>')
def uploads(filename):
    return send_from_directory(app.config['UPLOAD_PATH'],
                               filename)


@app.route("/home")
@app.route('/')
@register_breadcrumb(app, '.', 'Home')
def home():
    skills = list(mongo.db.skills.find())
    education = list(mongo.db.education.find().sort("order", 1))
    experience = list(mongo.db.experience.find().sort("order", 1))
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
def login_required(flash_message=False):
    """Function decorator to check for login

    Args:
        flash_message (bool, optional): Message to be sent via Flash. If left empty then no message is sent. Defaults to False.
    """
    def inner_function(f):
        """Wrapper function in order to get argument into decorator

        Args:
            f (function): Decorated function

        Returns:
            function: Function after being decorated
        """
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not session.get("user"):
                flash(flash_message) if flash_message else None
                return redirect(url_for("login"))
            else:
                return f(*args, **kwargs)
        return decorated_function
    return inner_function


@app.route('/admin')
@login_required()
def admin():
    return render_template("admin/dashboard.html")


@app.route('/admin/testimonials', methods=['GET', 'POST'])
@login_required("You don't have the user privileges to access this section.")
def get_testimonials():
    if request.method == "POST":
        testimonials = list(mongo.db.testimonials.find())

        for testimonial in testimonials:
            if request.form.get("approved[{}]".format(testimonial['_id'])):
                is_approved = True
            else:
                is_approved = False
            mongo.db.testimonials.update({"_id": ObjectId(testimonial['_id'])}, {
                "$set": {"approved": is_approved}})
        flash("Testimonials were successfully updated!")
        # Redirect to avoid re-submission
        return redirect(url_for("get_testimonials"))

    approved = list(mongo.db.testimonials.find({"approved": True}))
    unapproved = list(mongo.db.testimonials.find({"approved": False}))
    return render_template("admin/testimonials.html", approved=approved, unapproved=unapproved)


@app.route('/admin/delete_testimonial/<id>')
@login_required("You don't have the user privileges to access this section.")
def delete_testimonial(id):
    mongo.db.testimonials.remove({"_id": ObjectId(id)})
    flash("Testimonial was successfully deleted")
    return redirect(url_for("get_testimonials"))


@app.route('/admin/blogs')
@login_required("You don't have the user privileges to access this section.")
def get_blogs():
    blogs = list(mongo.db.blogs.find())
    return render_template("admin/blogs.html", blogs=blogs)


@app.route('/admin/add_blog', methods=["GET", "POST"])
@login_required("You don't have the user privileges to access this section.")
def add_blog():
    if request.method == "POST":
        uploaded_file = request.files['photo']
        filename = ''
        if uploaded_file.filename != '':
            new_filename = request.form.get(
                "slug")[:25] + str(random.randint(1111, 9999))
            file_ext = os.path.splitext(uploaded_file.filename)[1]
            if file_ext.lower() in app.config['UPLOAD_EXTENSIONS']:
                filename = new_filename + file_ext.lower()
                uploaded_file.save(os.path.join(
                    app.config['UPLOAD_PATH'], filename))
            else:
                flash("Uploaded file not supported!")

        blog = {
            "title": request.form.get("title"),
            "slug": request.form.get("slug"),
            "photo": filename,
            "body": request.form.get("body"),
            "added_on": date.today().strftime("%B %d, %Y")
        }
        mongo.db.blogs.insert_one(blog)
        flash(Markup(
            "Blog <strong>{}</strong> was successfully Added!".format(blog['title'])))
        return redirect(url_for("get_blogs"))

    return render_template("admin/add_blog.html")


@app.route('/admin/edit_blog/<id>', methods=["GET", "POST"])
@login_required("You don't have the user privileges to access this section.")
def edit_blog(id):
    post = mongo.db.blogs.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        if 'blog-data' in request.form:
            updated = {
                "title": request.form.get("title"),
                "slug": request.form.get("slug"),
                "body": request.form.get("body")
            }
            flash(Markup(
                "Blog <strong>{}</strong> was successfully edited!".format(updated['title'])))
        elif 'blog-photo' in request.form:
            uploaded_file = request.files['photo']
            filename = ''
            if uploaded_file.filename != '':
                new_filename = post["slug"][:25] + \
                    str(random.randint(1111, 9999))
                file_ext = os.path.splitext(uploaded_file.filename)[1]
                if file_ext.lower() in app.config['UPLOAD_EXTENSIONS']:
                    # remove current photo
                    if post["photo"].strip() and os.path.exists(os.path.join("uploads", post["photo"])):
                        os.remove(os.path.join("uploads", post["photo"]))
                    filename = new_filename + file_ext.lower()
                    uploaded_file.save(os.path.join(
                        app.config['UPLOAD_PATH'], filename))
                else:
                    flash("Uploaded file not supported!")
            else:
                # remove current photo
                if post["photo"].strip() and os.path.exists(os.path.join("uploads", post["photo"])):
                    os.remove(os.path.join("uploads", post["photo"]))

            updated = {
                "photo": filename
            }
            flash(Markup(
                "Blog <strong>{}</strong> was successfully edited!".format(post['title'])))
        else:
            flash("Something went wrong!")
            return redirect(url_for("get_blogs"))

        mongo.db.blogs.update({"_id": ObjectId(id)}, {
            "$set": updated})
        # Redirect to avoid re-submission
        return redirect(url_for("get_blogs"))

    return render_template("admin/edit_blog.html", post=post)


@app.route('/admin/delete_blog/<id>')
@login_required("You don't have the user privileges to access this section.")
def delete_blog(id):
    post = mongo.db.blogs.find_one({"_id": ObjectId(id)})
    if post["photo"].strip() and os.path.exists(os.path.join("uploads", post["photo"])):
        os.remove(os.path.join("uploads", post["photo"]))

    mongo.db.blogs.remove({"_id": ObjectId(id)})
    flash("Blog was successfully deleted")
    return redirect(url_for("get_blogs"))


@app.route('/admin/skills', methods=['GET', 'POST'])
@login_required("You don't have the user privileges to access this section.")
def get_skills():
    skills = list(mongo.db.skills.find())

    if request.method == "POST":
        for skill in skills:
            updated = {
                "name": request.form.get("name[{}]".format(skill['_id'])),
                "percentage": int(request.form.get("percentage[{}]".format(skill['_id'])))
            }
            mongo.db.skills.update({"_id": ObjectId(skill['_id'])}, {
                "$set": updated})

        flash("Skills were successfully updated!")
        # Redirect to avoid re-submission
        return redirect(url_for("get_skills"))

    return render_template("admin/skills.html", skills=skills)


@app.route('/admin/delete_skill/<id>')
@login_required("You don't have the user privileges to access this section.")
def delete_skill(id):
    mongo.db.skills.remove({"_id": ObjectId(id)})
    flash("Skill was successfully deleted")
    return redirect(url_for("get_skills"))


@app.route('/admin/add_skill', methods=["GET", "POST"])
@login_required("You don't have the user privileges to access this section.")
def add_skill():
    if request.method == "POST":
        skill = {
            "name": request.form.get("name"),
            "percentage": int(request.form.get("percentage"))
        }
        mongo.db.skills.insert_one(skill)
        flash(Markup(
            "Skill <strong>{}</strong> was successfully Added!".format(skill['name'])))
        return redirect(url_for("get_skills"))

    return render_template("admin/add_skill.html")


@app.route('/admin/education', methods=["GET", "POST"])
@login_required("You don't have the user privileges to access this section.")
def get_education():
    education = list(mongo.db.education.find().sort("order", 1))

    if request.method == "POST":
        for school in education:
            mongo.db.education.update({"_id": ObjectId(school['_id'])}, {
                "$set": {"order": int(request.form.get("order[{}]".format(school['_id'])))}})

        flash("Education successfully updated!")
        # Redirect to avoid re-submission
        return redirect(url_for("get_education"))

    return render_template("admin/education.html", education=education)


@app.route('/admin/add_education', methods=["GET", "POST"])
@login_required("You don't have the user privileges to access this section.")
def add_education():
    if request.method == "POST":
        school = {
            "school": request.form.get("school"),
            "period": request.form.get("period"),
            "title": request.form.get("title"),
            "department": request.form.get("department"),
            "description": request.form.get("description"),
            "order": int(request.form.get("order"))
        }
        mongo.db.education.insert_one(school)
        flash(Markup(
            "School <strong>{}</strong> was successfully Added!".format(school['school'])))
        return redirect(url_for("get_education"))

    return render_template("admin/add_education.html")


@app.route('/admin/edit_education/<id>', methods=["GET", "POST"])
@login_required("You don't have the user privileges to access this section.")
def edit_education(id):
    if request.method == "POST":
        updated = {
            "school": request.form.get("school"),
            "period": request.form.get("period"),
            "title": request.form.get("title"),
            "department": request.form.get("department"),
            "description": request.form.get("description"),
            "order": int(request.form.get("order"))
        }
        mongo.db.education.update({"_id": ObjectId(id)}, {
            "$set": updated})
        flash(Markup(
            "School <strong>{}</strong> was successfully edited!".format(updated['school'])))
        # Redirect to avoid re-submission
        return redirect(url_for("get_education"))

    school = mongo.db.education.find_one({"_id": ObjectId(id)})
    return render_template("admin/edit_education.html", school=school)


@app.route('/admin/delete_education/<id>')
@login_required("You don't have the user privileges to access this section.")
def delete_education(id):
    mongo.db.education.remove({"_id": ObjectId(id)})
    flash("School was successfully deleted")
    return redirect(url_for("get_education"))


@app.route('/admin/experience', methods=["GET", "POST"])
@login_required("You don't have the user privileges to access this section.")
def get_experience():
    experience = list(mongo.db.experience.find().sort("order", 1))

    if request.method == "POST":
        for job in experience:
            mongo.db.experience.update({"_id": ObjectId(job['_id'])}, {
                "$set": {"order": int(request.form.get("order[{}]".format(job['_id'])))}})

        flash("Work Experience successfully updated!")
        # Redirect to avoid re-submission
        return redirect(url_for("get_experience"))

    return render_template("admin/experience.html", experience=experience)


@app.route('/admin/add_experience', methods=["GET", "POST"])
@login_required("You don't have the user privileges to access this section.")
def add_experience():
    if request.method == "POST":
        job = {
            "company": request.form.get("company"),
            "period": request.form.get("period"),
            "role": request.form.get("role"),
            "description": request.form.get("description"),
            "order": int(request.form.get("order"))
        }
        mongo.db.experience.insert_one(job)
        flash(Markup(
            "Job at <strong>{}</strong> was successfully Added!".format(job['company'])))
        return redirect(url_for("get_experience"))

    return render_template("admin/add_experience.html")


@app.route('/admin/edit_experience/<id>', methods=["GET", "POST"])
@login_required("You don't have the user privileges to access this section.")
def edit_experience(id):
    if request.method == "POST":
        updated = {
            "company": request.form.get("company"),
            "period": request.form.get("period"),
            "role": request.form.get("role"),
            "description": request.form.get("description"),
            "order": int(request.form.get("order"))
        }
        mongo.db.experience.update({"_id": ObjectId(id)}, {
            "$set": updated})
        flash(Markup(
            "Job at <strong>{}</strong> was successfully edited!".format(updated['company'])))
        # Redirect to avoid re-submission
        return redirect(url_for("get_experience"))

    job = mongo.db.experience.find_one({"_id": ObjectId(id)})
    return render_template("admin/edit_experience.html", job=job)


@app.route('/admin/delete_experience/<id>')
@login_required("You don't have the user privileges to access this section.")
def delete_experience(id):
    mongo.db.experience.remove({"_id": ObjectId(id)})
    flash("Job was successfully deleted")
    return redirect(url_for("get_experience"))


@app.route('/admin/projects')
@login_required("You don't have the user privileges to access this section.")
def get_projects():
    projects = list(mongo.db.projects.find())
    return render_template("admin/projects.html", projects=projects)


@app.route('/admin/add_project', methods=["GET", "POST"])
@login_required("You don't have the user privileges to access this section.")
def add_project():
    if request.method == "POST":
        project = {
            "title": request.form.get("title"),
            "slug": request.form.get("slug"),
            "tech": request.form.get("tech"),
            "description": request.form.get("description"),
            "repo": request.form.get("repo"),
            "live_url": request.form.get("live_url"),
            "photos": request.form.get("photos")
        }
        mongo.db.projects.insert_one(project)
        flash(Markup(
            "Project <strong>{}</strong> was successfully Added!".format(project['title'])))
        return redirect(url_for("get_projects"))

    return render_template("admin/add_project.html")


@app.route('/admin/edit_project/<id>', methods=["GET", "POST"])
@login_required("You don't have the user privileges to access this section.")
def edit_project(id):
    if request.method == "POST":
        updated = {
            "title": request.form.get("title"),
            "slug": request.form.get("slug"),
            "tech": request.form.get("tech"),
            "description": request.form.get("description"),
            "repo": request.form.get("repo"),
            "live_url": request.form.get("live_url"),
            "photos": request.form.get("photos")
        }
        mongo.db.projects.update({"_id": ObjectId(id)}, {
            "$set": updated})
        flash(Markup(
            "Project <strong>{}</strong> was successfully edited!".format(updated['title'])))
        # Redirect to avoid re-submission
        return redirect(url_for("get_projects"))

    project = mongo.db.projects.find_one({"_id": ObjectId(id)})
    return render_template("admin/edit_project.html", project=project)


@app.route('/admin/delete_project/<id>')
@login_required("You don't have the user privileges to access this section.")
def delete_project(id):
    mongo.db.projects.remove({"_id": ObjectId(id)})
    flash("Project was successfully deleted")
    return redirect(url_for("get_projects"))


@app.route('/admin/links', methods=['GET', 'POST'])
@login_required("You don't have the user privileges to access this section.")
def get_links():
    links = list(mongo.db.links.find())

    if request.method == "POST":
        for link in links:
            updated = {
                "name": request.form.get("name[{}]".format(link['_id'])),
                "icon": request.form.get("icon[{}]".format(link['_id'])),
                "url": request.form.get("url[{}]".format(link['_id']))
            }
            mongo.db.links.update({"_id": ObjectId(link['_id'])}, {
                "$set": updated})

        flash("Links were successfully updated!")
        # Redirect to avoid re-submission
        return redirect(url_for("get_links"))

    return render_template("admin/links.html", links=links)


@ app.route('/admin/delete_link/<id>')
@login_required("You don't have the user privileges to access this section.")
def delete_link(id):
    mongo.db.links.remove({"_id": ObjectId(id)})
    flash("Link was successfully deleted")
    return redirect(url_for("get_links"))


@ app.route('/admin/add_link', methods=["GET", "POST"])
@login_required("You don't have the user privileges to access this section.")
def add_link():
    if request.method == "POST":
        link = {
            "name": request.form.get("name"),
            "icon": request.form.get("icon"),
            "url": request.form.get("url")
        }
        mongo.db.links.insert_one(link)
        flash(Markup(
            "Link <strong>{}</strong> was successfully Added!".format(link['name'])))
        return redirect(url_for("get_links"))

    return render_template("admin/add_link.html")


@ app.route('/admin/settings', methods=["GET", "POST"])
@login_required("You don't have the user privileges to access this section.")
def settings():
    if request.method == "POST":
        updated = {
            "name": request.form.get("name"),
            "bio": request.form.get("bio"),
            "status": request.form.get("status"),
            "availability": request.form.get("availability"),
            "email": request.form.get("email"),
            "phone": request.form.get("phone"),
            "address": request.form.get("address"),
            "photo": request.form.get("photo"),
            "cv": request.form.get("cv"),
            "meta_title": request.form.get("meta_title"),
            "meta_desc": request.form.get("meta_desc"),
            "meta_keys": request.form.get("meta_keys")
        }
        mongo.db.settings.update({"_id": ObjectId(os.environ.get("DB_SETTINGS_ID"))}, {
            "$set": updated})
        flash("Settings were successfully updated!")
        # Redirect to avoid re-submission
        return redirect(url_for("settings"))

    return render_template("admin/settings.html")


@ app.route('/admin/login', methods=["GET", "POST"])
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


@ app.route("/admin/logout")
def logout():
    if session.get("user"):
        session.pop("user")

    flash("You have been logged out")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
