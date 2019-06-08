# Takes in first, middle, and last name, and returns an email address for the user. 

from sys import argv
script, first, middle, last = argv

email = f"{first}_{middle}_{last}@gmail.com"
print(email.lower())

