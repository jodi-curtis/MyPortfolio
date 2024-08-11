# Project Class
class Project:
    def __init__(self, id: int, name: str, year: str, image: str, images: list[str], link: str, languages: list[int], brief: str, description: str):
        self.id = id
        self.name = name
        self.year = year
        self.image = image
        self.images = images
        self.link = link
        self.languages = languages
        self.brief = brief
        self.description = description

# Create list of project objects
projects = [
    Project(
        id=1,
        name='Jazz Fanzz',
        year='2024',
        image='jazz_fanzz.jpg',
        images=['jazz_fanzz.jpg'],
        link='https://jodi-curtis.github.io/',
        languages=[1, 2],
        brief="A website to learn more about the Jazz music genre.",
        description=(
            "Jazz Fanzz is a website designed for fans of jazz music and those interested in finding out more about the genre.\n\nI developed this website for the Web Design Assessment as part of the UCD Full Stack Software Development Course.\n\nThe Jazz Fanzz website is a user-friendly website with engaging design and can be used to learn about the history of jazz, listen to music, and find out about upcoming jazz music events.\n\nThe website consists of 4 pages: Home, About, Artists, and Events."
        )
    ),
    Project(
        id=2,
        name='Maths Playground',
        year='2024',
        image='maths_playground.jpg',
        images=['maths_playground.jpg'],
        link='https://jodi-curtis.github.io/maths-playground/',
        languages=[1, 2, 3],
        brief='An interactive website for kids to learn about and test their knowledge on basic Maths concepts.',
        description=(
            "Maths Playground is a website designed for young children to help them learn basic maths concepts.\n\nI developed this website for the Javascript Assessment as part of the UCD Full Stack Software Development Course.\n\nThe Maths Playground website provides kids with interactive tools to help them learn and quizzes where they can test their knowledge.\n\nThe website has 4 pages: Learn, Quiz, Results, and Feedback."
        )
    ),
    Project(
        id=3,
        name='Mannok Pack Picker App',
        year='2020',
        image='picker_app.jpg',
        images=['picker_app.jpg'],
        link='',
        languages=[1, 2, 3, 4],
        brief='Web Application designed for use on a tablet to assist with the picking of loads.',
        description=(
            "The Mannok Pack Picker App is a Web-Based application designed to assist with the picking of loads within the Packaging division of Mannok.\n\nI developed this Web App during my year-long placement at Mannok.\n\nThe app runs on a tablet in a forklift in the Packaging warehouse and allows pickers to see what needs to go on each load without the need for paper pick lists.\n\nThe Web App consists of 3 pages: Login, List, and Details."
        )
    ),
    Project(
        id=4,
        name='Recycling Assistant',
        year='2022',
        image='recycling_assistant.jpg',
        images=['recycling_assistant.jpg'],
        link='',
        languages=[5],
        brief='Mobile App which provides information to make recycling easier.',
        description=(
            "The Recycling Assistant App is a Mobile App designed to help users make better decisions when it comes to Recylcing.\n\nI developed this App for my Final Year Project as part of my Computer Science Degree.\n\nThe App was created using Andriod Studio.\n\nRecycling Assistant allows user to scan the barcodes of different products and it tells them whether the packaging is recyclable or not. The app also allows users to set up reminders to perform recycling activities."
        )
    )
]

