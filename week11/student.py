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


	# DON'T DO THIS!
	# def __init__(self, name, id, grades=[]):

	# 	self.name = name
	# 	self.id = id
	# 	self.grades = grades