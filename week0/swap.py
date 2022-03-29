num1 = float(input("Choose first number: "))
num2 = float(input("Choose second number: "))

holder = num1
num1 = num2
num2 = holder
print("After swap...")
print("number 1: " + str(num1))
print("number 2: " + str(num2))