from flask import Flask, render_template
from grades import grades, highest_grade, lowest_grade

app = Flask(__name__)

projects = [
    {'id': 1, 'name': 'Jazz Fanzz', 'image': 'jazz_fanzz.jpg', 'brief':"A website to learn more about the Jazz music genre..", 'description': 'Jazz Fanzz is a website designed for fans of jazz music and those interested in finding out more about the genre. The Jazz Fanzz website can be used to learn about the history of jazz, listen to music and find out about upcoming jazz music events. It is a user friendly website with engaging design. The website consists of 4 pages: Home, About, Artists and Events.'},
    {'id': 2, 'name': 'Maths Playground', 'image': 'maths_playground.jpg', 'brief': 'An interactive website for kids to learn about and test their knowledge on basic Maths concepts..', 'description': 'Maths Playground is designed for young children to help them learn basic maths concepts by giving them interactive tools to help them learn and quizzes where they can test their knowledge. The website has 4 pages: Learn, Quiz, Results and Feedback.'},
    {'id': 3, 'name': 'Mannok Pack Picker App', 'image': 'picker_app.jpg', 'brief': 'Web Application designed for use on a tablet to assist with the picking of loads..', 'description': 'Description of Project Three'}
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