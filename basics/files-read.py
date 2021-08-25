# file path should be relative to the execution context.
# Here i'm trying to runt he program from root directory and so traversing the path
filePath = "files/fruits.txt"

# myFile = open(filePath)
# content = myFile.read()
# myFile.close()

# print(content)

# other way to read is
with open(filePath) as myFile:
    content2 = myFile.read()

print(content2)
