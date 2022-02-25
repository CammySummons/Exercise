class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # Integer 0-100

    # Method to return student grade
    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []  # To hold students

    # Method to add students to the course
    def add_student(self, student):
        # Test that there is room in the class
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True  # Where student added
        return False  # Where student not added

    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade()
            return total / len(self.students)


# Main routine

# Instantiate 3 student objects
s1 = Student("Tim", 19, 95)
s2 = Student("Bell", 19, 75)
s3 = Student("Caleb", 19, 65)

# Instantiate course object
course1 = Course("Computer Science", 3)

# Add students to course
course1.add_student(s1)
course1.add_student(s2)
print(course1.add_student(s3))

# Get average grade of all students in a course
print(f"The average grade in {course1.name} is "
      f"{course1.get_average_grade()}")









# class Dog:
#     def __init__(self, name, age, colour):
#         self.name = name
#         self.age = age
#         self.colour = colour
#
#     def print_details(self):
#         return f"{self.name} is a {self.colour} dog aged {self.age}"
#
#     def change_age(self, age):
#         self.age = age
#
#
# # Main routine
# dog1 = Dog("Spot", 7, "Gay")
# dog2 = Dog("Jazz", 21, "Black")
# print(Dog.print_details(dog1))
# print(Dog.print_details(dog2))
#
# dog1.change_age(17)
# dog2.change_age(9)
#
# print(Dog.print_details(dog1))
# print(Dog.print_details(dog2))
