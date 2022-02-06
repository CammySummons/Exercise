name = ""
greatest_name = ""
uni_grade = ""
greatest_mark = 0
divider = 0
mark_total = 0
count = -1  # Keeps track of what place items from lists are
names_list = []
marks_list = []


while name != "X":
    mark = -1
    name = input("Student name: ")
    while mark > 100 and name != "X" or mark < 0 and name != "X":
        mark = int(input("Exam mark: "))
    if name == "X":
        mark = 0
        divider -= 1
    divider += 1
    mark_total += mark
    names_list.append(name)
    marks_list.append(mark)
    if name == "X":
        names_list.remove(names_list[-1])
        marks_list.remove(marks_list[-1])

    if mark > greatest_mark:
        greatest_mark = mark
        greatest_name = name

print("\nBest student: {}\n"
      "Student mark: {}\n"
      "Average mark: {}\n"
      "\n--Student grade list--"
      .format(greatest_name, greatest_mark, mark_total/divider))

for item in names_list:
    count += 1
    if marks_list[count] >= 90:
        uni_grade = "A+"
    elif 89 >= marks_list[count] >= 85:
        uni_grade = "A"
    elif 80 <= marks_list[count] <= 84:
        uni_grade = "A-"
    elif 75 <= marks_list[count] <= 79:
        uni_grade = "B+"
    elif 70 <= marks_list[count] <= 74:
        uni_grade = "B"
    elif 65 <= marks_list[count] <= 69:
        uni_grade = "B-"
    elif 60 <= marks_list[count] <= 64:
        uni_grade = "C+"
    elif 55 <= marks_list[count] <= 59:
        uni_grade = "C"
    elif 50 <= marks_list[count] <= 54:
        uni_grade = "C-"
    elif 40 <= marks_list[count] <= 49:
        uni_grade = "D"
    elif 0 <= marks_list[count] <= 39:
        uni_grade = "E"
    print("Student: {}     Mark: {}     University Grade: {}"
          .format(names_list[count], marks_list[count], uni_grade))
