
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))

# A replica of if-then-else
if first > second and first > third:
    print(first, " is the gratest number")

#elif is a substitute of Then in computer theory
elif second > first and second > third:
    print(second, " is the gratest number")

else:
    print(third, " is the gratest number")