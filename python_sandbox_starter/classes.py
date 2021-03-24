# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class User:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Methods
    def greeting(self):
        return f"My name is {self.name} and I am {self.age}"

    def has_birthday(self):
        self.age += 1


# Init User Obj
halit = User("Halit Oskan", 41)

halit.has_birthday()
print(halit.greeting())
