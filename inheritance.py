#Parent Class/ Superclass/ Base Class
class Animal:
    isMammal = True

    def speak(self):
        print("Animal is speaking")

    def move(self):
        print("Animal is moving")

# Child class/ subclass / derived class
class Cat(Animal):

    def sound(self):
        print("Cat is meowing")

    def climb(self):
        print("Cat is climbing trees")




class horse(Animal):

    hasTail = True

    def neigh(self):
        print("Horse is neighing")


# Creating objets from the classes

a = Animal() # Object 1
a.speak()
a.move()

c = Cat() # Object 2
c.climb()
c.sound()

h = horse() # Object 3
h.neigh()



