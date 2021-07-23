f=open("text.txt")
fileLines = f.readlines()
for line in fileLines:
    print(line)

string = "My Name Is Swastik. I Study In 9th Grade"
words = string.split()
print(words)

string2 = "My Name Is Swastik, I Study In 9th Grade"
words2 = string2.split(",")
print(words2)

def countWords():
    pass