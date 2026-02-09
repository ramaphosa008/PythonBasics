# FUNCTIONS/ METHODS(e.g. len() )- a block of code that runs when called upon

#1. Standard-Library functions
y = max(45, 46, 83, 84, 83, 97, 53, 43)
print("The max number is", y)

x = min(784, 67893, 44, 35, 9454, 345)
print("THe min number is", x)

print()

#2. User-defined functions
     #Example 1
def name():
    print("Cyril")

name()

print()

        #Exampple 2
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))
print(fahrenheit_to_celsius(122))

print()

       #Example 3
def add ():
    print(10+20)

add()

print()

        #OR
def type():
    x = int(input("Please enter a value x :"))
    y = int(input("Please enter a value y :"))
    print("The sum of x amd y is", x + y)

type()

print()

# Use of variables - Limits user to enter details of only  one dog
def dogdetails():
    name = "Rocky"
    breed = "Siberian Husky"
    age = 3
    print(name, breed, age)

    print()

# Use of parameters
def dogs(name, breed, sex, age):
    print(name, breed, sex, age)
    
dogs("Rocky", "Husky", "Male", 3)
dogs("Crusher", "Bulldog", "Female", 4)

def students( name, age, agenda):
    print(name, age, agenda)