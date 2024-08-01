from flask import Flask, render_template

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
    return render_template("about.html")

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