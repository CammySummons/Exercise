class AllStaff:
    def __init__(self, name, age, id, birthdate, job):
        self.name = name
        self.age = age
        self.id = id
        self.birthdate = birthdate
        self.job = job


class Management(AllStaff):
    def __init__(self, name, age, id, birthdate, job, car):
        super().__init__(name, age, id, birthdate, job)
        self.car = car

    def show(self):
        print(f"Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"ID: {self.id}\n"
              f"Birthdate: {self.birthdate}\n"
              f"Job: {self.job}\n"
              f"Car: {self.car}")


class Clerical(AllStaff):
    def __init__(self, name, age, id, birthdate, job, typing_speed):
        super().__init__(name, age, id, birthdate, job)
        self.typing_speed = typing_speed

    def show(self):
        print(f"Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"ID: {self.id}\n"
              f"Birthdate: {self.birthdate}\n"
              f"Job: {self.job}\n"
              f"Typing speed: {self.typing_speed}")


class Factory(AllStaff):
    def __init__(self, name, age, id, birthdate, job):
        super().__init__(name, age, id, birthdate, job)

    def show(self):
        print(f"Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"ID: {self.id}\n"
              f"Birthdate: {self.birthdate}\n"
              f"Job: {self.job}")

