from zoneinfo import reset_tzpath

num1 = float(input("Enter the first value: "))
operator = input("Enter the operator((+, -, /, *): ")
num2 = float(input("Enter the second value: "))

if operator == "+":
    answer = num1 + num2
    print("The answer is: ", answer)

elif operator == "-":
    answer = num1 - num2
    print("The answer is: ", answer)


elif operator == "*":
    answer = num1 * num2
    print("The answer is: ", answer)

elif operator == "/":
    if num2 != 0:
        answer = num1 / num2
        print("The answer is: ", answer)
    else:
        print("Cannot divide by zero!")

else:
    answer = "Math Error!"

