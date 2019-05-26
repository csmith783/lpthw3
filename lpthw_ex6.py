# Exercise 6
# Strings and Text

# Defines the 'types_of_people' variable and sets it equal to 10
types_of_people = 10

# Creates an f-string which uses the 'types_of_people' variable
x = f"There are {types_of_people} types of people."

# Simple string assignment
binary = "binary"
do_not = "don't"

# Creates an f-string 
y = f"Those who know {binary} and those who {do_not}."

# Print the strings
print(x)
print(y)

# Creates f-strings
print(f"I said: {x}")
print(f"I also said: '{y}")

# Creates the 'hilarious' variable and sets it equal to False, a boolean value 
hilarious = False

# Creates a string with an empty formatter
joke_evaluation = "Isn't that joke so funny? {}"

# Prints the string, and references the '.format()' method
# to populate the previously empty formatter
print(joke_evaluation.format(hilarious))

# Simple string assignment
w = "This is the left side of a ...."
e = "string with a right side."

# Print the concatenated strings 
print(w + e)