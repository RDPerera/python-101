sampleWritingFile = open("resources/sampleWrite.txt", "a")


content = "This is a sample file for writing.\nHello world\n"
sampleWritingFile.write(content)

sampleWritingFile.close()