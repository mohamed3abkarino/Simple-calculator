print("Calculator: enter any two numbers.")

n1 = float(input("Enter your first number: "))
operation = input("Enter the operation (+, -, ×, or ÷): ")
n2 = float(input("Enter your second number: "))

if operation == "addition" or "+":
    print(n1 + n2)

elif operation == "subtraction" or operation == "-": 
    print(n1 - n2)

elif operation == "multiplication" or operation == "x" or operation == "×":
    print(n1 * n2)

elif operation == "division" or operation == "/" or operation == "÷":
    print(n1 / n2)

else:
    print("Error")