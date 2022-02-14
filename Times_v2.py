times_100m = []
times_200m = []
times_400m = []
valid = False
loop = True
track_type = ""
go = "Y"  # Decides whether to loop grab_times or not


def print_results(tracks):
    total = 0
    fastest = 10000000
    for result in tracks:
        print(f"- {result}s")
        total += int(result)
        if fastest > result:
            fastest = result

    average = total/len(tracks)

    print(f"Fastest time: {fastest}s")
    print(f"Average time: {average}s\n")


def grab_times(times):
    time = ""
    fastest = 100000
    while time != -1:
        time = int(input("Enter a time (or type -1 to finish): "))
        if time != -1:
            times.append(time)

    total = 0
    print("---Times---")
    for item in times:
        print(item)
        total += int(item)
        if fastest > item:
            fastest = item

    average = total/len(times)

    print(f"Fastest time: {fastest}")
    print(f"Average time: {average}")
    proceed = input("Do you want to enter more times? (Y/N): ").upper()
    return proceed


# Getting track type and running grab_times function
while go != "N":
    track_type = input("What track type? (100m, 200m, 400m): ")
    if track_type == "100m":
        go = grab_times(times_100m)

    elif track_type == "200m":
        go = grab_times(times_200m)

    elif track_type == "400m":
        go = grab_times(times_400m)

# Printing results
while loop:
    result_selection = input("Which track results would you like to view?"
                             " (You can also press 'c' to clear data "
                             "and -1 to exit): ")
    if result_selection == "100m" and times_100m != []:
        print("\n**** 100m Track Times ****")
        print_results(times_100m)
    elif result_selection == "200m" and times_200m != []:
        print("\n**** 200m Track Times ****")
        print_results(times_200m)
    elif result_selection == "400m" and times_400m != []:
        print("\n**** 400m Track Times ****")
        print_results(times_400m)
    elif result_selection.lower() == "c":
        # Decides if you want to clear data
        while not valid:
            clear = input("Enter track type for data you want to clear (else enter -1): ")
            if clear == "100m":
                times_100m = []
                print("Times cleared")
                valid = True
            elif clear == "200m":
                times_200m = []
                print("Times cleared")
                valid = True
            elif clear == "400m":
                times_400m = []
                print("Times cleared")
                valid = True

    elif result_selection == "-1":
        loop = False
    else:
        print("\nNo times to display\n")
