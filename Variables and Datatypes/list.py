# Mutable Datatype : Each element in the list can be changed.
# Iterable : We can loop through each element in the list.

listOfNumbers = [11, 12, 13, 14, 15]

# Accessing Elements
print(listOfNumbers[1]) # Output: 12
print(listOfNumbers[1:4]) # Output: [12, 13, 14]
print(listOfNumbers)

# Modifying Elements

listOfNumbers[1] = 22 #Mutating the list : Mutable Datatype
print(listOfNumbers) # Output: [11, 22, 13, 14, 15]

# Adding Elements

listOfNumbers.append(16) # Adding an element to the end of the list
print(listOfNumbers) # Output: [11, 22, 13, 14, 15, 16]

listOfNumbers.insert(2, 23) # Adding an element at a specific index
print(listOfNumbers) # Output: [11, 22, 23, 13, 14, 15, 16]

# Length of the List
print(len(listOfNumbers)) # Output: 7


withAllDataTypes = [1, 2, 3, 4, 5, 'apple', 'banana', 'cherry', [6, 7, 8, 9, 10], {'name':'John','age':25}, True, False, None, 1+2j]
print(withAllDataTypes[8][2])
