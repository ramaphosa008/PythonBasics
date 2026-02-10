class employee:

    def __init__(self, fullname, position, status, age):   #self - refers to a specific object

        # Attributes
        self.fullname = fullname
        self.position = position
        self.status = status
        self.age = age

    def work(self):
        print(self.fullname, "is working")


employee1 = employee("John Mwirigi", "Managing Director", "Marrried", 57)


print()

print(employee1.fullname, employee1.position, employee1.status, employee1.age)

print()

employee1.work()

print()

employee2 = employee("Jean Kamau", "Program Director", "Single", 34)

print()

print(employee2.fullname)
print(employee2.position)
print(employee2.status)
print(employee2.age)

print()

employee2.work()


employee3 = employee('Mark Joe', "Lecturer", "Single", 32)

