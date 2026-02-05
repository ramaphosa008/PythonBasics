# ARITHMETIC OPERATORS
x = 20
y = 6

print(x + y)

print(x - y)

print(x / y)

print(x * y)

print(x % y) #Modulus - returns remainder after


#COMPARISON OPERATORS - all about comparing
print(x < y)

print(x > y)

print(x <= y)

print(x >= y)

print(x == y) #Equal to

print(x != y)  # ! - represents 'NOT' in the defined comparison


#ASSIGNMENT OPERATORS - used to assign/store values in variables
# (=)
number = 45
print(number)

#(+)
number += 2
print(number)

#(-)
number -= 2
print(number)

#(*)
number *= 2
print(number)

#(**)
number **= 2
print(number)

#LOGICAL OPERATORS
num1 = 67
num2 = 43

#AND - returns true if all/both conditions are true, returns false if one condition is a false.
print(num1 == num2 and num1 > num2)

#OR - returns True if one of the statements is true, returns false if both conditions are false
print(num1 == num2 or num1 > num2)

#NOT - Reverse the result, returns False if the result is true
print(not (num1 == num2 or num1 > num2))
print(not (num1 == num2 and num1 > num2))
