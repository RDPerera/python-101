# Stings

# Immutable - Strings are immutable, which means that once they are created, they cannot be changed.
# Iterable - Strings are iterable, which means that we can iterate over the characters in a string.


# Creating a string
# Strings can be created by enclosing characters inside single quotes or double quotes.


# Not valid 
# sampleString = ""Hello World""
# sampleString = ''Hello World''

# Valid
# sampleString = "Hello World"
# sampleString = 'Hello World'
# sampleString = '''Hello World'''
# sampleString = """Hello World"""

# Accessing characters in a string
# sampleString = "Hello World"

# Accessing the first character
# print(sampleString[0]) # Output: H
# print(sampleString[-11]) # Output: H

# Getting the length of a string
# print(len(sampleString)) # Output: 11

# stringLength = len(sampleString)
# print(stringLength) # Output: 11


# Accessing the last character
# lastChar = sampleString[len(sampleString)-1]
# print(lastChar) # Output: d

# print(sampleString[len(sampleString)-1]) # Output: d


# Slicing a string
# Syntax: string[startIndex:endIndex:step]
# default step is 1
# default startIndex is 0
# default endIndex is length of string

# sampleString = "Hello World"
# sliceString = sampleString[0:5]
# print(sliceString) # Output: Hello

# sliceString = sampleString[6:11]
# print(sliceString) # Output: World

# sliceString = sampleString[0:11:2]
# print(sliceString) # Output: HloWrd

# sliceString = sampleString[6:]
# print(sliceString) # Output: World

# sliceString = sampleString[:-2]
# print(sliceString) # Output: Hello Wor

# sliceString = sampleString[::2]
# print(sliceString) # Output: HloWrd

# sliceString = sampleString[::-1]
# print(sliceString) # Output: dlroW olleH

# sliceString = sampleString[::]
# print(sliceString) # Output: Hello World

# String Concatenation
# sampleString1 = "Hello"
# sampleString2 = "World" 
# concatString = sampleString1 + sampleString2
# print(concatString) # Output: HelloWorld
# print(sampleString1 + sampleString2) # Output: HelloWorld
# print(sampleString1 + " " + sampleString2) # Output: Hello World
# print("Hello" + " " + "World") # Output: Hello World



# This is not a valid concatenation
# This is just printing two strings
# print(sampleString1,sampleString2) # Output: Hello World
# print("Hello",10) # Output: Hello 10
# concatString = "hello" + 10 # This will throw an error

# String Repetition
# sampleString = "Hello"
# repeatedString = sampleString * 3
# print(repeatedString) # Output: HelloHelloHello
# print(sampleString * 3) # Output: HelloHelloHello

# String Split
# sampleString = "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
# splitString = sampleString.split()
# # default separator is space
# print(splitString) # Output: ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'sed', 'do', 'eiusmod', 'tempor', 'incididunt', 'ut', 'labore', 'et', 'dolore', 'magna', 'aliqua']

# splitString = sampleString.split("e")
# print(splitString) # Output: ['Lor', 'm ipsum dolor sit am', 't cons', 'ct', 'tur adi', 'scing ', 'lit s', 'd do ', 'iusmod t', 'mpor incididunt ut labor', ' ', 't dolor', ' magna aliqua']

# sampleString = "HelloWorld"
# splitString = sampleString.split("W")
# print(splitString) # Output: ['Hello', 'orld']

# sampleCSVString = "John,Doe,25,New York"
# splitString = sampleCSVString.split(",")
# print(splitString) # Output: ['John', 'Doe', '25', 'New York']

# String Strip
# sampleString = "   Hello World   "
# stripString = sampleString.strip()