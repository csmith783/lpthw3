# Exercise 13
# Parameters, Unpacking, and Variables 
# Arguments are another way to pass input into your script. 

# Import sys to be able to use argv
from sys import argv

# unpack the command line parameters and assign them to variables. 
script, first, second, third = argv

# Print out the variables
print("The script is called:", script)
print("The first variable is:", first)
print("The second variable is:", second)
print("The third variable is:", third)

# Prompt the user for input
middle_name = input("What is your middle name? ")

# Create a formatter and use the Format method to pass in values. 
print("Total inputs are {} {} {} {} {}.".format(script, first, second, third, middle_name))