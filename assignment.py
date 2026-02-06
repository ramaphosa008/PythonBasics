# Consider INDENTATION since it signifies a certain block of code.
number = int(input("Enter a certain number: "))

if number == 0:
    print("The number is neutral")

elif number % 2 == 0:
    print(f"{number} is an even number")

else:
    print(f"{number} is an odd number")