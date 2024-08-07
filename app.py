from flask import Flask, render_template
from grades import grades, highest_grade, lowest_grade
from languages import languages


app = Flask(__name__)

projects = [
    {'id': 1, 
     'name': 'Jazz Fanzz', 
     'year': '2024', 
     'image': 'jazz_fanzz.jpg', 
     'link': 'https://jodi-curtis.github.io/',
     'languages': [1, 2],
     'brief':"A website to learn more about the Jazz music genre..", 
     'description': 'Jazz Fanzz is a website designed for fans of jazz music and those interested in finding out more about the genre.\n \nI developed this website for the Web Design Assessment as part of the UCD Full Stack Software Development Course. \n\nThe Jazz Fanzz website is a user friendly website with engaging design and can be used to learn about the history of jazz, listen to music and find out about upcoming jazz music events.\n\nThe website consists of 4 pages: Home, About, Artists and Events.'
     },
    {'id': 2, 
     'name': 'Maths Playground', 
     'year': '2024', 
     'image': 'maths_playground.jpg', 
     'link': 'https://jodi-curtis.github.io/maths-playground/',
     'languages': [1, 2, 3],
     'brief': 'An interactive website for kids to learn about and test their knowledge on basic Maths concepts..', 
     'description': 'Maths Playground is a website designed for young children to help them learn basic maths concepts. \n\nI developed this website for the Javascript Assessment as part of the UCD Full Stack Software Development Course. \n\nThe Maths Playground website provides kids with interactive tools to help them learn and quizzes where they can test their knowledge. \n\nThe website has 4 pages: Learn, Quiz, Results and Feedback.'
     },
    {'id': 3, 
     'name': 'Mannok Pack Picker App', 
     'year':'2022', 
     'image': 'picker_app.jpg',
     'link': '',
     'languages': [1, 2, 3, 4],
     'brief': 'Web Application designed for use on a tablet to assist with the picking of loads..', 
     'description': 'The Mannok Pack Picker App is a Web Based application designed to assist with the picking of loads within the Packaging division of Mannok. \n\n I developed this Web App durinng my year long placment at Mannok. \n\nThe app runs on a tablet in a forklift in the Packaging warehouse and allows pickers to see what needs to go on each list without the need of paper pick lists. \n\nThe Web App consits of 3 pages: Login, List, and Details.'
     }
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
    project_languages = [l for l in languages if l['key'] in project['languages']]
    return render_template('project_detail.html', project=project, languages=project_languages)