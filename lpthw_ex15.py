# Exercise 15
# Reading Files

from sys import argv

script, filename = argv

# Open the file given on the command line and return a file object 
txt = open(filename)

print(f"Here's your file {filename}:")

# Call the read method on the fiel object - returns the files data; this is all returned to the print statement 
print(txt.read())

# Close the file object - best practice 
txt.close()

# print("Type the file name again:")
# file_again = input(">> ")

# text_again = open(file_again)
# print(text_again.read())