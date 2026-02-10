# You can set default values for __init__ method

class boys:
    def __init__(self, name, age, gender="male"):
        self.name = name
        self.age = age
        self.gender = gender

boy1 = boys("Joe", 19)

boy2 = boys("Fredrick", 17, "male")

print(boy1.name, boy1.age, boy1.gender)
print(boy2.name, boy2.age, boy2.gender)


# Modifying class properties outside the parameters

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print(p1.age)

p1.age = 26
print(p1.age)
