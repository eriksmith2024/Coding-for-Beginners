class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Robot:
    def speak(self):
        return "Beep bop!"

# Polymorphism: different objects, same method name
things = [Dog(), Cat(), Robot()]

for thing in things:
    print(thing.speak())
