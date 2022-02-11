time = ""
times = []
fastest = 0

while time != -1:
    time = int(input("Enter a time (or type -1 to finish): "))
    if time != -1:
        times.append(time)

total = 0
print("---Times---")
for item in times:
    print(item)
    total += int(item)
    if fastest < item:
        fastest = item

average = total/len(times)

print(f"Fastest time: {fastest}")
print(f"Average time: {average}")
