# If else statement
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if number1 > number2:
    print(number1)
else:
    print(number2)

# If elif else statement  
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# Multiple elif statement
marks=int(input("Input marks: "))
if marks >= 75:
    print("A")
elif marks >=65:
    print("B")
elif marks >=55:
    print("C") 
elif marks >=35:
    print("S")
else: 
    print("W")

# Nested if else statement
number1=int(input("enter first number: "))
number2=int(input("enter second number: "))
number3=int(input("enter third number: "))
 
if number1 > number2:
    if number1 > number3:
        print("Number ",number1,"is biggest.")
    else:
        print("Number ",number3,"is biggest.")
else:
    if number2>number3:
        print("Number ",number2,"is biggest.")
    else:
        print("Number ",number3,"is biggest.")

# Doing the same thing with boolean operators
number1=int(input("enter first number: "))
number2=int(input("enter second number: "))
number3=int(input("enter third number: "))

if number1 > number2 and number1 > number3:
    print("Number ",number1,"is biggest.")
elif number2>number3:
    print("Number ",number2,"is biggest.")
else:
    print("Number ",number3,"is biggest.")