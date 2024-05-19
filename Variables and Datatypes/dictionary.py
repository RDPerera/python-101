# Dictionary is a collection of key-value pairs. It is unordered, changeable and indexed.

# Iterable
# Mutable
# Key-Value pairs

dict1 = {
    'name': 'John',
    'age': 25,
    'city': 'New York',
    'country': 'USA',
    'telephone-numbers': [123456, 789101]
}

dict2 = {"name":'John', "age":25, "city":'New York', "country":'USA'}

print(dict1)  # {'name': 'John', 'age': 25, 'city': 'New York', 'country': 'USA'}

# Accessing the value using the key
print(dict1['name'])  # John

# .values() method
print(dict1.values())  # dict_values(['John', 25, 'New York', 'USA'])

# .keys() method
print(dict1.keys())  # dict_keys(['name', 'age', 'city', 'country'])