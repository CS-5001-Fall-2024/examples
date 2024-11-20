import json
from student import Student
"""
"cs5001": [
        {
            "name": "Igor",
            "grades": [100, 100, 78, 92],
            "id": 54321
        }
    ],
"""

with open('students.json') as students:
    data = json.load(students)
    students_list = []
    course_roster = data['cs5001']
    for student in course_roster:
        # print(student)
        name = student['name']
        grades = student['grades']
        id = student['id']
        next_student = Student(name, grades, id)
        students_list.append(next_student)

for student in students_list:
    print(student)

    # data['cs5001'][1]['grades'].append(98)
    #print(data['students'][1]['id'])