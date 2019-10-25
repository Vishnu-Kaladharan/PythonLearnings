class Mammal:
    no_of_legs = 4

    def walk(self):
        print('Walk')


class Dog(Mammal):
    def __init__(self, dog_name):
        self.type = dog_name

    def bark(self):
        print(f"Bark {self.type}")


dog1 = Dog('Jacky')
dog1.bark()
dog1.walk()
print(dog1.no_of_legs)