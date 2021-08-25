# file path should be relative to the execution context.
# Here i'm trying to runt he program from root directory and so traversing the path
fruitsPath = "files/fruits.txt"
firstPath = "files/first.txt"

# myFile = open(filePath)
# content = myFile.read()
# myFile.close()

# print(content)

# other way to read is
with open(fruitsPath) as fruits:
    content2 = fruits.read()

with open(firstPath, "w") as first:
    first.write(content2 + "\n")

with open(firstPath, 'a+') as first:
    first.write("done!")
    first.seek(0)
    print(first.read())
