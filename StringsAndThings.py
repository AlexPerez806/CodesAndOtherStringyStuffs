# Strings

# Concatenation
#     2 or more strings and put them together

firstName = "Wilma"
lastName = "Flintstone"

print(firstName + " " + lastName)

name = firstName + " " + lastName
lastFirst = lastName + ", " + firstName

print(lastFirst)

# Repetition

#   repetition operator: *

print("Hip "*2 + "Hooray!")

def rowYourBoat():
    print("Row, "*3 + "your boat")
    print("Gently down the stream")
    print("Merrily, "*4)
    print("Life is but a dream")

rowYourBoat()

# Indexing

name = "Roy G Biv"
firstChar = name[0]
print(firstChar)

middleCharIndex = len(name) // 2
print(middleCharIndex)
print(name[middleCharIndex])

print(name[-3])

for i in range(0, len(name)):
    print(name[i])

# Slicing and dicing

print(name[-4:8])

for i in range(0, len(name)+1):
    print(name[0:i])

# Searching

if "y" not in name:
   print("biv" in name)
else:
   print("y" not in name)


















# Character functions

print(chr(104))
print(ord('&'))


