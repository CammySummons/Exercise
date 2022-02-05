name = ""
greatest_mark = 0
greatest_name = ""
divider = 0
mark_total = 0


while name != "X":
    name = input("Student name: ")
    mark = int(input("Exam mark: "))
    if name == "X":
        mark = 0
    divider += 1
    mark_total += mark

    if mark > greatest_mark:
        greatest_mark = mark
        greatest_name = name

print("\nBest student: {}\n"
      "Student mark: {}\n"
      "Average mark: {}\n"
      .format(greatest_name, greatest_mark, mark_total/divider))
