# Set is a collection of unique elements. It is unordered and unindexed. Sets are written with curly brackets.

# Non-indexed
# Immutable

set1 = {3, 2, 1, 4, 5, 6, 7, 8, 9, 10}
print(set1)  # {'Microsoft', 'Google', 'Apple'}

set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

set3 = set1.union(set2)
print(set3)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


set4 = set1.intersection(set2)
print(set4)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

set5 = set1.difference(set2)
print(set5)  # set()

l1 = list(set1)