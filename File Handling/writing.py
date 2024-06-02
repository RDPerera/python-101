sampleWritingFile = open("resources/sampleWrite.txt", "w")
content = "This is a sample file for writing.\nHello world\n"
sampleWritingFile.write(content)


print("Content written to file.",file=sampleWritingFile)

sampleWritingFile.close()