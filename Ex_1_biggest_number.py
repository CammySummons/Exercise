num1 = 1
num2 = 1

while num1 != 0 or num2 != 0:
    num1 = int(input("What is the first number: "))
    num2 = int(input("What is the second number: "))
    if num2 > num1:
        print(f"The biggest number is {num2}\n")
    elif num1>num2:
        print(f"The biggest number is {num1}\n")
    else:
        print("Numbers are equal\n")
