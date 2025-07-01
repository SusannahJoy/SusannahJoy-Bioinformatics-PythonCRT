class Person:
    def __init__(self):
        pass
    def details(self):
        print("Name, Age, Gender")
class Student(Person):
    def __init__(self):
        pass
    def student_info(self):
        print("Grade: 10th")
class Teacher(Person):
    def __init__(self):
        pass
    def teacher_info(self):
        print("Teaches Mathematics")
class TeachingAssistant(Teacher, Student):
    def assist(self):
        print("Assists the teacher in class")
T1=TeachingAssistant()
T1.assist()