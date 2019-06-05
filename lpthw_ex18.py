# Exercise 18
# Names, Variables, Code, Functions 

# this one is like your script with argv
# 'def' kicks off a fucntion, all indented lines that follow will be part of the function. 
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# Ok, that *args is actually pointless, we can just do this. 
# function takes in two arguments, no need to unpack when done this way. 
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
# takes in on argument 
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nuthin!")

# Call all the functions. 
print_two("San", "Antonio")
print_two_again("San", "Antonio")
print_one("First!")
print_none()
