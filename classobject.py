# CLASS - is a blueprint of an object (what each an every object should be having)
# OBJECT -

class student:
    #Attributes
    name = "Joy"
    age = 20
    gender = "Female"
    course = "MIT"

    # Behavior is written as a function
    def  study(self):
        print("Student is studying")

# An object is represented by a variable - CREATING AN OBJECT
student1 = student()

# Calling a function
student1.study()

# To display a value contained in a variable, use PRINT
print(student1.name)

student2 = student()

student3 = student()
print(student3.gender)




