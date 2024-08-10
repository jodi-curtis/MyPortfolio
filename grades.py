# List of grades
grades = [
    {"subject": "Mathmatics for Computing", "grade": 98},
    {"subject": "Software Development 1", "grade": 94},
    {"subject": "Systems Analysis and Design", "grade": 80},
    {"subject": "Software Development 2", "grade": 85},
    {"subject": "Database Systems", "grade": 74},
    {"subject": "Hardware amd Operating Systems", "grade": 80},
    {"subject": "Computer Networks and Security", "grade": 76},
    {"subject": "UX", "grade": 64},
    {"subject": "Object Orientated Programming", "grade": 96},
    {"subject": "Algorithms and Data Structures", "grade": 73},
    {"subject": "Web Application Development", "grade": 90},
    {"subject": "Mobile Application Development", "grade": 82},
    {"subject": "Professional Issues", "grade": 66},
    {"subject": "Cyber Security", "grade": 62},
    {"subject": "Network Operating Systems", "grade": 70},
    {"subject": "Mobile Technology", "grade": 82},
    {"subject": "Intelligent Robotics", "grade": 95},
    {"subject": "Final Year Project", "grade": 66}
]

# Function to find highest scoring grade
def highest_grade():
    highest = max(grades, key=lambda x: x['grade'])
    return highest

# Function to find lowest scoring grade
def lowest_grade():
    lowest = min(grades, key=lambda x: x['grade'])
    return lowest