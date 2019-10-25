class Person:

    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f'Talk {self.name}')


person1 = Person('Vishnu')
person2 = Person('Varun')

person2.talk()
person1.talk()

