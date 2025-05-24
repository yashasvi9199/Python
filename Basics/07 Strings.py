# Python offers two declaration for strings. Assignment and tripple quotes.
## Assignment operator
a = " HELLO "
b = ' hello '

## Tripple Quotes
"""
This is
a multi line string function. 
Unless assigned to a variable, 
this will be a junk string which is inaccessible by program and thus treated as comment
"""

humpa = '''multi line string 
that is assigned
 to a variable'''

# Printing whole string
print (a,b,humpa, sep="\n")

# printing every character
for character in a:
    print(character)

# creating function to print every char in string (since is works just like an array of char data)

def printChar(char):
    print("Printing characters")
    for characters in char:
        print (characters)

print("\n")
printChar(a)
printChar(b)
printChar(humpa)