class Person:
  species = "Human"  # Class property - are properties defined outside methods and belong to the class itself

  def __init__(self, name):
    self.name = name  # Instance property- belong to each object

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)



# ADDITION OF NEW PROPERTIES

class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)