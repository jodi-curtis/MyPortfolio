from flask import Flask, render_template
from grades import grades, highest_grade, lowest_grade

app = Flask(__name__)

projects = [
    {'id': 1, 'name': 'Project One', 'description': 'Description of Project One'},
    {'id': 2, 'name': 'Project Two', 'description': 'Description of Project Two'},
    {'id': 3, 'name': 'Project Three', 'description': 'Description of Project Three'}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    highest = highest_grade()
    lowest = lowest_grade()
    return render_template("about.html", grades = grades, highest = highest, lowest = lowest)

@app.route("/projects")
def project_list():
    return render_template("projects.html", projects=projects)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/project/<int:project_id>')
def project_details(project_id):
    project = next((p for p in projects if p['id'] == project_id), None)
    return render_template('project_detail.html', project=project)