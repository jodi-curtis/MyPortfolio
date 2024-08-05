grades = [
    {"subject": "Math", "grade": 95},
    {"subject": "Science", "grade": 89},
    {"subject": "English", "grade": 92},
    {"subject": "History", "grade": 88},
    {"subject": "Art", "grade": 99}
]

def highest_grade():
    highest = max(grades, key=lambda x: x['grade'])
    return highest

def lowest_grade():
    lowest = min(grades, key=lambda x: x['grade'])
    return lowest
