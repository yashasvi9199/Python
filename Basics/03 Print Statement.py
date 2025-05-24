print("HIHIHIHI")
# Simple print statement. Nothing fancy

print ("Hello World", "I am learning Python")
# Printing multiple strings in one line. They can be files, variables and response from a function or object

print("Hello World","I am learning Python", sep=", ")
# Printing multiple strings in one line with a separator. The default separator is a space

print("Hello World","I am learning Python", sep=", ", end=".\n")
# Printing multiple strings in one line with a separator and an end character. The default end character is a new line
# In a situation where we are printing multiple lines, we can use the end character to print the next line in the same line OR

print("Hello World","I am learning Python", sep=", ", end=". Kudos\n")
# Print something specific at the end of the line.

# Without the end character, the next print statement will be printed in a new line anyways. It is just a matter of how we want to format the output.
# The end character can be a space, a new line, a tab, a comma, a period, etc. It can be anything we want.
print("Hello World","I am learning Python", sep=", ")
print("Hello World","I am learning Python", sep=", ", end=".\n")