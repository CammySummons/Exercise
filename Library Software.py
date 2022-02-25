class Book:
    def __init__(self, title, author, dewey, isbn):
        self.title = title.title()
        self.borrower = None
        self.author = author
        self.dewey = dewey
        self.isbn = isbn
        self.available = True
        book_list.append(self)  # Holds book objects

    def book_info(self):
        print(self.title)
        print(self.author)
        print(self.dewey)
        print(self.isbn)
        print(self.available)
        print(self.borrower)
        print("########################")


class User:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.fees = 0.0
        self.borrowed_book = []
        user_list.append(self)

    def user_details(self):
        print("Name: ", self.name)
        print("Address: ", self.address)
        print("Fees $", self.fees)
        print("#########################")


def print_user():
    for i in user_list:
        i.user_details()


def add_book():
    title = input("Enter the new book's title: ").title()
    author = input("Enter the new book's author: ").title()
    dewey = input("Enter the new book's dewey code: ").upper()
    isbn = input("Enter the new book's ISBN: ")
    Book(title, author, dewey, isbn)
    print(f"{title} has been added to the book list")


def print_info():
    for book in book_list:
        book.book_info()


# Adding a book
def add_user():
    name = input("What is your name: ").title()
    address = input("What is your address: ")
    User(name, address)
    print(name, address, "has been added to the user list")


# Find a user
def find_user():
    user_to_find = input("Enter the name of the user: ").title()
    for user in user_list:
        if user.name == user_to_find:
            print(f"Hi {user_to_find}")
            return user
    print("Sorry, no user was found with that name")
    return None


# Find a book
def find_book():
    book_to_find = input("Enter the name of the book: ").title()
    for book in book_list:
        if book.title == book_to_find:
            print(f"The book '{book_to_find}' is in the catalogue")
            return book
    print("Sorry, no book was found with that name")
    return None


def lend_book():
    user = find_user()
    print()
    if user:  # Only if user was found
        book = find_book()
        if book.available:
            confirm = input("Type 'y' if you want to borrow this book: ").upper()

            if confirm == "Y":
                print(f"Book title: '{book.title}' is now out on loan to '{user.name}'")
                book.available = False
                book.borrower = user.name
                user.borrowed_book.append(book.title)
        else:
            print(f"sorry, '{book.title}' is already out on loan")


def return_book():
    user = find_user()
    print()
    if user:
        book = find_book()
        if not book.available:
            confirm = input("Type 'Y' if you want to return this book").upper()
            if confirm == "Y":
                print(f"Book title: '{book.title}' is now returned to the library")
                book.available = True
                book.borrower = user.name
                user.borrowed_books.remove(book.title)
        else:
            print(f"Sorry, '{book.title}' on loan to someone else")


# Main routine
book_list = []
user_list = []

# Book objects
Book("Lord of the rings", "J.R.R. Tolkien", "TOL", "9780261103252")
Book("Random", "Jack Jack", "JAC", "9973487845876")
Book("Potato", "Pop Pops", "POP", "9749386734989")
Book("Protector of the object", "Jr. Tank", "TAN", "93485972657843")

# User objects
User("John", "12 Example St")
User("Sammy", "21 Brahman Cl")
User("Paul", "420 Apple Dr")
User("Potato", "Nonexistent Pl")

# User menu
new_action = True
while new_action:
    print("1. Lend a book")
    print("2. Return a book")
    print("3. Add a user")
    print("4. Add a book")
    print("5. Exit")

    choice = input("\nWhat would you like to do? - enter a number: ")
    if choice == "1":
        lend_book()
    elif choice == "2":
        return_book()
    elif choice == "3":
        add_user()
    elif choice == "4":
        add_book()
    elif choice == "5":
        confirm = input("Type 'Y' if you want to exit the system - or any other key to go back to the menu: ").upper()
        if confirm == "Y":
            print("Goodbye")
            new_action = False
    else:
        print("\n *** That was not a valid choice ***\n")

# find_book()
# find_user()
# add_book()
# print_info()
# add_user()
# print_user()
