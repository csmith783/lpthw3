# Exercise 32
# Loops and Lists

the_count = [ 1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for loop goes through lists 
for number in the_count:
    print(f"This is count {number}.")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lsits too
# notice we have to use {} since we dont know what is in it
for i in change:
    print(f"I got {i}")

# we can also build lists, but first create an empty one 
elements = []
 
# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")
