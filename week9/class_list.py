from student import Student

# create three students

student1 = Student('Edwin', 12345 , 'male')
student2 = Student('Sami', 98765 , 'female')

# add grades for each student
student1.add_grade(100)
student1.add_grade(98)

student2.add_grade(78)
student2.add_grade(54)

print(str(student1))
print(student2)

student2.id = 87654
student2.set_id(34567)

print(student2)