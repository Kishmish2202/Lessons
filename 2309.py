class Animal():
    def __init__ (self, name, color):
        self.name = name
        self.color = color
    def sleep(self):
        print(f'{self.name} Zoo....')
    def eat(self):
        print(f'{self.name} On now now.....')
#class Cat(Animal):
#    pass

#fluffy = Animal('Snowball', 'while')
#fluffy.sleep()
#fluffy.eat()

#smokey = Cat('Smokey','grey')
#smokey.sleep()
#smokey.eat()

class Cat(Animal):
    def say(self):
        print(f'{self.name} Meow!!!')

class Dog(Animal):
    def say(self):
        print(f'{self.name} Bark!!!')

fluffy = Cat('Snowball','while')
fluffy.say()

cooper = Dog('Cooper','red')
cooper.say()