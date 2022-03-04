class Student:
    def __init__(self, name, age, phone_num, form_cls, subjects, is_male):
        self.name = name
        self.age = age
        self.phone_num = phone_num
        self.form_cls = form_cls
        self.subjects = subjects
        self.is_male = is_male
        self.enrolled = True
        student_list.append(self)

    def display_info(self):
        print("\n##################\n")
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Phone number: " + self.phone_num)
        print("Form class: " + self. form_cls)
        print("Subjects: " + self.subjects)
        if self.is_male:
            print(f"{self.name} is male")
        else:
            print(f"{self.name} is female")
        print(f"Enrolled: {self.enrolled}")


class Teacher:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects
        teacher_list.append(self)

    def display_info(self):
        print("\n##################\n")
        print(f"Name: {self.name}")
        print(f"Subjects: {self.subjects}")


# Printing all students
def print_student_details():
    for student in student_list:
        Student.display_info(student)


# Printing all teachers
def print_teacher_details():
    for teacher in teacher_list:
        Teacher.display_info(teacher)


# Print students with a specified gender
def get_gender():
    valid = False
    count = 0
    while not valid:
        count = 0
        gender = input("Gender (male/female): ")
        for student in student_list:
            if gender == "male" and student.is_male:
                print(student.name)
                count += 1
                valid = True
            elif gender == "female" and not student.is_male:
                print(student.name)
                count += 1
                valid = True
        if not valid:
            print("Not a valid gender!")
    print(f"Number of students: {count}")


# Printing students above a certain age
def select_student_age():
    student_num = 0
    for student in student_list:
        if student.age > 17:
            student_num += 1
            Student.display_info(student)
    print(f"\nTotal number of students above 17 years old: {student_num}")


# Getting student objects from file
def generate_students():
    import csv
    with open('random_students.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter='|')
        for line in filereader:
            if line[5] == "True":
                is_male = True
            else:
                is_male = False
            Student(line[0], int(line[1]), line[2], line[3], line[4], is_male)


# Counting number of students in a subject
def count_students():
    student_total = 0
    what_class = input("\nWhat class are you looking for?: ")
    for student in student_list:
        if what_class in student.subjects:
            print(student.name)
            student_total += 1
    if student_total == 0:
        print("There are no students in this class")
    else:
        print(f"\nTotal number of students: {student_total}")
    for teacher in teacher_list:
        if what_class == teacher.subjects:
            print(f"Teacher: {teacher.name}")


# Getting student and their details
def find_student():
    student_name = input("\nWhat is the student's name?: ")
    found = False
    for student in student_list:
        if student.name.lower() == student_name.lower():
            Student.display_info(student)
            found = True

    if not found:
        print("Student not found")


# Adding a student
def add_student():
    name = input("Name: ").title()
    age = is_integer(input("Age: "))
    phone_num = input("Phone Number: ")
    form_cls = input("Form Class: ")
    subjects = input("Subjects: ")
    is_male = input("Gender: ")
    Student(name, age, phone_num, form_cls, subjects, is_male)
    print(name, "has been added to the user list")


# Removing a student
def remove_student():
    valid = False
    name = input("Enter the name of the student you wish to remove: ")
    for student in student_list:
        if name == student.name:
            while not valid:
                confirm = input(f"Are you sure you want to purge {student.name}? (y/n): ").lower()
                if confirm == "y":
                    print(f"\n-{student.name} has been removed from the system-")
                    student_list.remove(student)
                    valid = True
                elif confirm == "n":
                    valid = True
                else:
                    valid = False


# Integer checker
def is_integer(text):
    valid = False
    while not valid:
        try:
            number_to_check = int(input(text))
            if isinstance(number_to_check, int):
                valid = True
                return number_to_check
        except ValueError:
            print("You must enter a whole number!\n")


# Main Menu
def menu():
    valid = False
    while not valid:
        valid = False
        print("\n-----Main Menu-----\n"
              "1. Count Students Taking a Particular Subject\n"
              "2. Print a Full List of All Students\n"
              "3. Print a List of Students Above a Particular Age\n"
              "4. Get Details of a Particular Student\n"
              "5. Add Student\n"
              "6. Remove Student\n"
              "7. Print Teachers\n"
              "8. Print Students of a Specified Gender")
        select = input("What would you like to do? (Note: "
                       "Enter 'Q' to exit or a number to select an option): ")
        if select == "1":
            count_students()
        elif select == "2":
            print_student_details()
        elif select == "3":
            select_student_age()
        elif select == "4":
            find_student()
        elif select == "5":
            add_student()
        elif select == "6":
            remove_student()
        elif select == "7":
            print_teacher_details()
        elif select == "8":
            get_gender()
        elif select == "Q":
            valid = True
        else:
            print("That is not a valid input!\n")


# Main routine
student_list = []
teacher_list = []
generate_students()

# Instantiating teacher objects
tea1 = Teacher("Baker", "GRA")
tea2 = Teacher("Barker", "MAT")
tea3 = Teacher("Graham", "BIO")
tea4 = Teacher("Morgan", "DTC")
tea5 = Teacher("Bell", "PHY")
tea6 = Teacher("Nimmo", "ART")
tea7 = Teacher("McNicol", "ENG")

menu()

