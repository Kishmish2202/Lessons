class Cat():
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def sleep(self):
        print(f'{self.name} Zzz...')
    def eat(self):
        print(f'{self.name} Om now now...')


fluffy = Cat('Snowball', 'white')
print(fluffy.name)
print(fluffy.color)
fluffy.sleep()
fluffy.eat()

