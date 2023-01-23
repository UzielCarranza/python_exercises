
class Dog:
    # self is a reference to the current instance of the class
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
    # methods need to be on the same level as the class
    def speak(self):
            print(self.name + ' says woof')


my_Dog = Dog('Fido', 4)

my_Dog.speak();