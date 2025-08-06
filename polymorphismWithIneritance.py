class Animal: # Animal class is the first instance from which the other animals are created
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):
        return "Woof!" # The speak method changing - polymorphing

class Cat(Animal):
    def speak(self):
        return "Meow!" # The speak method changing - polymorphing

# Polymorphism in action
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    print(animal.speak())
