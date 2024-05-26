# for i in range(1,11):
#     print(i)

# for i in range(1,11,2):
#     print(i)

# Multiplication table of 13
# for i in range(1,13):
#     print("13 X",i,"=",13*i)

# Single hill star pattern
# for i in range(1, 6):
#     print(" "*(5-i)+"*"*(2*i-1))

# Reverse hill star pattern
# for i in range(5, 0, -1):
#     print(" "*(5-i)+"*"*(2*i-1))

#Double hill star pattern
# for i in range(1, 6):
#     print(" "*(5-i)+"*"*(2*i-1)+" "*(11-2*i)+"*"*(2*i-1))

# Print odd numbers from 1 to 10
# for i in range(10):
#     if i%2==1:
#         print(i)

# Print triangle of numbers
# output = 0
# for i in range(1,11):
#     output = output + i
#     print(output)

# Print sum of odd numbers from 1 to n
# givenInput=int(input("Enter a number: "))
# sum=0
# for i in range(1,givenInput+1,2):
#     sum = sum + i
#     print("i=",i,"sum=",sum,"input=",givenInput)
# print(sum)

# Factorial of 1,10
# for i in range (1,11):
#     factorial=1
#     for j in range(1,i+1):
#         factorial = factorial * j
#     print(factorial)

# Check whether a number is a prime or not
# status="This is a Prime"
# givenNumber=int(input("Enter number: "))
# for i in range(2,givenNumber):
#     if givenNumber%i == 0 :
#         status="This is not a Prime"
# print(status)


# Print prime numbers though 1 to n
# limit = int(input("Enter the end of number range: "))
# for checkingNumber in range(1,limit):
#     isPrime = True
#     for divider in range(2,checkingNumber):
#         if checkingNumber%divider == 0:
#             isPrime = False
#     if isPrime:
#         print(checkingNumber)
