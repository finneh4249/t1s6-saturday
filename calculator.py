# Simple calculator using if-else statements

print('Simple Calculator', '\n')
# Get user inputs
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+,-,*,/): ")
num2 = float(input("Enter second number: "))

# Perform calculations
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("YOU CAN'T DIVIDE BY ZERO YOU STUPID LITTLE FOOL!")
        exit()
    else:
        result = num1 / num2
else:
    print("Invalid operator")
    exit()

# Print result

if result % 1 == 0:
    result = int(result)

print('\n', num1, operator, num2, '=', result)

