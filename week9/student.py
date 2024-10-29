class Student:
    """A class to represent information about a student.
    """

    def __init__(self, name, id, gender):
        """Constructor.
        Initialize properties name, id, and gender based on parameters.
        Initialize grades to an empty list.
        """
        self.name = name
        self.id = id
        self.gender = gender
        self.grades = []


    def add_grade(self, grade):
        """Add a new grade.
        Parameter:
          grade (float): new grade to be added
        """
        if grade > 0:
            self.grades.append(grade)
        # print(self.grades)


    def set_id(self, id):
        """Update student id.
        Parameter:
          id (int): updated id  
        """
        self.id = id


    def __str__(self):
        return f'{self.name} - {self.id} - {self.grades}'