class Student:

	def __init__(self, name: str, id: int, grades = None):

		self.name = name
		self.id = id

		if not grades: # grades == None:
			self.grades = []
		else:
			self.grades = grades

	def __str__(self):
		return f'Name: {self.name} - ID: {self.id} - Grades: {self.grades}'

# s1 = Student('Bob', 1234)
# s2 = Student('Jane', 9076, [82])
# s3 = Student('Sally', 1375)
# s4 = Student('Herb', 2932)
# s1.grades.append(95)
# print(s1.grades)
# print(s2.grades)
# print(s3.grades)


	# DON'T DO THIS!
	# def __init__(self, name, id, grades=[]):

	# 	self.name = name
	# 	self.id = id
	# 	self.grades = grades