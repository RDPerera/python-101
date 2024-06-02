sampleFile = open("resources/sample.txt", "r")
lines = sampleFile.read()
print(lines)

for i in range(2):
    print(sampleFile.readline().strip())

sampleFile.close()