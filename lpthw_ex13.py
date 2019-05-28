# Exercise 13
# Parameters, Unpacking, and Variables 
# Arguments are another way to pass input into your script. 

from sys import argv
script, first, second, third = argv

print("The script is called:", script)
print("The first variable is:", first)
print("The second variable is:", second)
print("The third variable is:", third)

middle_name = input("What is your middle name? ")

print("Total inputs are {} {} {} {} {}.".format(script, first, second, third, middle_name))