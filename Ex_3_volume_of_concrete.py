depth = 0
width = 0
length = 0
concrete_volume = 0
concrete_volume_total = 0
building_type = ""
valid = False

while length != "X" or width != "X" or building_type != "X":
    length = int(input("What is the length: "))
    width = int(input("What is the width: "))

    while not valid:
        building_type = input("What is the building type: ")
        if building_type == "residential":
            depth = 0.25
            valid = True
        elif building_type == "commercial":
            depth = 0.5
            valid = True
        else:
            print("Invalid building type!")

    concrete_volume = length*width*depth
    concrete_volume_total += concrete_volume
    print("\nThe volume of concrete required for a slab with a length of {}, a"
          " width of {} and a depth of {} is {} cubic metres"
          .format(length, width, depth, concrete_volume))
    print("Total concrete volume required for all buildings: {} cubic metres\n"
          .format(concrete_volume_total))
