class Animal:
    def __init__ (self, name:str):
        self.name = name
    def sound (self):
        pass
    
class Dog(Animal):
        def sound (self):
            print ("Guau")
    
class Cat(Animal):
        def sound (self):
            print("miau")
    
my_animal = Cat.sound("Toby")