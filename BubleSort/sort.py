numbers = [11,22,10,33,12,45,56,32,23]

for i in range(len(numbers)):
    for j in range (0, len(numbers)-i-1):
        if numbers[j] > numbers[j+1]:
            temp=numbers[j+1]
            numbers[j+1]=numbers[j]
            numbers[j]=temp

print(numbers)