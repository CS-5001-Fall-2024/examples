import unittest
from student import Student

class StudentTest(unittest.TestCase):

    def test_constructor_name(self):
        s = Student('name', 1234, 'female')
        self.assertEqual('name', s.name)

    def test_constructor_id(self):
        s = Student('name', 1234, 'female')
        self.assertEqual(1234, s.id)

    def test_constructor_gender(self):
        s = Student('name', 1234, 'female')
        self.assertEqual('female', s.gender)

    def test_constructor_grades(self):
        s = Student('name', 1234, 'female')
        self.assertEqual([], s.grades)

    def test_add_grade(self):
        s = Student('name', 1234, 'female')
        s.add_grade(100)
        self.assertEqual([100], s.grades)


    def test_add_grade_negative(self):
        s = Student('name', 1234, 'female')
        s.add_grade(-100)
        self.assertEqual([], s.grades)


def main():
    unittest.main()

if __name__ == '__main__':
    main()