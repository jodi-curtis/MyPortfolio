from flask import Flask, render_template, request, redirect, url_for
from grades import grades, highest_grade, lowest_grade
from languages import languages
from projects import projects


app = Flask(__name__)

# Home Page
@app.route("/")
def index():
    return render_template("index.html")

# About Page
@app.route("/about")
def about():
    # Get highest and lowest grades
    highest = highest_grade()
    lowest = lowest_grade()
    return render_template("about.html", grades = grades, highest = highest, lowest = lowest)

# Projects Page
@app.route("/projects")
def project_list():
    return render_template("projects.html", projects=projects)

# Project Detail Page
@app.route('/project/<int:project_id>')
def project_details(project_id):
    # Get selected project by ID
    project = next((p for p in projects if p.id == project_id), None)
    # If project found, get related languages
    if project:
        project_languages = [l for l in languages if l['key'] in project.languages]
    else:
        project_languages = []
    return render_template('project_detail.html', project=project, languages=project_languages)

# Contact Page
@app.route("/contact", methods=["GET","POST"])
def contact():
    # On Form submit
    if request.method == 'POST':
        # Get data entered in form
        fname = request.form.get('fname')
        sname = request.form.get('sname')
        email = request.form.get('email')
        subject = request.form.get('subject')

        # Reload Contact page with data from form
        return redirect(url_for('contact', success=True, fname=fname, sname=sname, email=email, subject=subject))
    
    # Get data from URL
    success = request.args.get('success')
    fname = request.args.get('fname')
    sname = request.args.get('sname')
    email = request.args.get('email')
    subject = request.args.get('subject')
    return render_template("contact.html", success=success, fname=fname, sname=sname, email=email, subject=subject)