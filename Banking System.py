class User:
    def __init__(self, first_name, last_name, gender, street_address, city,
                 email, cc_number, cc_type, balance, account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_no = account_no
        userList.append(self)
    
    def display_info(self):
        print("\n##############################\n")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Gender: {self.gender}")
        print(f"Street Address: {self.street_address}")
        print(f"City: {self.city}")
        print(f"Email: {self.email}")
        print(f"CC Number: {self.cc_number}")
        print(f"CC Type: {self.cc_type}")
        print(f"Balance: ${self.balance :.2f}")
        print(f"Account Number: {self.account_no}\n")

        
def generate_users():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6],
                 line[7], float(line[8][1:]), line[9])


def find_user():
    found = False
    name = input("User's name (first and last with space to separate): ")
    for user in userList:
        if name.lower() == f"{user.first_name} {user.last_name}".lower():
            User.display_info(user)
            found = True
    if not found:
        print("User not found!")


def overdrafts():
    count = 0
    overdraft_total = 0
    for user in userList:
        if user.balance < 0:
            print(f"- {user.first_name} {user.last_name}")
            overdraft_total += user.balance
            count += 1
    print(f"\nNumber of overdraft accounts: {count}")
    print(f"Total overdraft: ${overdraft_total :.2f}")

    
def missing_emails():
    count = 0
    for user in userList:
        if user.email == "":
            print(f"- {user.first_name} {user.last_name}")
            count += 1
    print(f"\nNumber of missing emails: {count}")


def bank_details():
    count = 0
    total_balance = 0
    lowest = 1000000000000000
    highest = -10000000000000
    highest_user_name = ""
    lowest_user_name = ""
    for user in userList:
        if lowest > user.balance:
            lowest = user.balance
            lowest_user_name = f"{user.first_name} {user.last_name}"
        if highest < user.balance:
            highest = user.balance
            highest_user_name = f"{user.first_name} {user.last_name}"
        total_balance += user.balance
        count += 1
    print(f"Total number of users: {count}")
    print(f"Total bank worth (sum of user balances): ${total_balance :.2f}")
    print("\n----Highest balance user----\n"
          f"Name: {highest_user_name}\n"
          f"Balance: ${highest}")
    print("\n----Lowest balance user----\n"
          f"Name: {lowest_user_name}\n"
          f"Balance: ${lowest}")


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


def transfer():
    # Basically all of these variables are stated at the start so python
    # doesn't say I referenced before assignment
    confirm = ""
    name_loss = ""
    name_gain = ""
    transfer_to = ""
    new_balance_loss = 0
    new_balance_gain = 0
    calc_new_balance_loss = 0
    calc_new_balance_gain = 0
    account_number = 0

    # Person who is transferring
    give_valid = False
    while not give_valid:
        account_number = input("Account Number: ")
        for user in userList:
            if account_number == user.account_no:
                give_valid = True
                User.display_info(user)
                name_loss = f"{user.first_name} {user.last_name}"
        if not give_valid:
            print("Account number invalid!\n")
    transfer_amount = is_integer("Transfer amount: $")

    # Person receiving transfer
    receive_valid = False
    while not receive_valid:
        transfer_to = input("Account to transfer to: ")
        for user in userList:
            if user.account_no == transfer_to:
                receive_valid = True
                name_gain = f"{user.first_name} {user.last_name}"
                confirm = input(f"Are you sure you want to transfer "
                                f"${transfer_amount :.2f} to {name_gain}? "
                                f"(y/n): ").lower()
        if not receive_valid:
            print("Account number invalid!\n")

    # Executing transfer
    if confirm == "y":
        for user in userList:
            if user.account_no == account_number:
                new_balance_loss = float(user.balance)
            if user.account_no == transfer_to:
                new_balance_gain = float(user.balance)

        for user in userList:
            if user.account_no == account_number:
                calc_new_balance_loss = new_balance_loss - transfer_amount
                user.balance = calc_new_balance_loss
            if user.account_no == transfer_to:
                calc_new_balance_gain = new_balance_gain + transfer_amount
                user.balance = calc_new_balance_gain
        print(f"- New bank balance of {name_loss}: "
              f"${calc_new_balance_loss :.2f}\n"
              f"- New bank balance of {name_gain}: "
              f"${calc_new_balance_gain :.2f}\n"
              f"Amount transferred: "
              f"${(new_balance_gain - calc_new_balance_gain) * -1 :.2f}")


# Main routine
userList = []
generate_users()

userChoice = ""
print("Welcome")

# Main menu
while userChoice != "Q":
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    userChoice = input("Enter choice: ")
    print()
    
    if userChoice == "1":
        find_user()
    elif userChoice == "2":
        overdrafts()
    elif userChoice == "3":
        missing_emails()
    elif userChoice == "4":
        bank_details()
    elif userChoice == "5":
        transfer()      
    print()
