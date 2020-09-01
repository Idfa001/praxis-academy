print("your very basic calculator")
print("")

num1 = float(input("Enter first number :"))
opr  = input("Enter operator :")
num2 = float(input("Enter second number :"))

if opr == "+":
    print(num1 + num2)
elif opr == "-":
    print(num1 - num2)
elif opr == "/":
    print(num1 / num2)
elif opr == "*":
    print(num1 * num2)
else:
    print("Invalid number or operator")