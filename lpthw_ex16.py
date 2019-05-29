# Exercise 16
# Reading and Writing Files

# Important File object commands
# close: closes the file, saves the file
# read: Reads the contents of the file, you can assign the results to a variable. 
# readline: reads just one line of text
# truncate: empties the file
# write('stuff'): writes 'stuff' to the file
# seek(0): moves the read/write location to the beginning of the file. 

from sys import argv
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C)")
print("If you do want that, hir RETURN.")
input("? ")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now i'm going to ask you for three lines.")

l1 = input("line 1: ")
l2 = input("line 2: ")
l3 = input("line 3: ")

print("I'm going to write these to the file.")

#target.write(l1)
#target.write("\n")
#target.write(l2)
#target.write("\n")
#target.write(l3)
#target.write("\n")

target.write(f"{l1}\n{l2}\n{l3}\n")

print("And finally, we close it.")
target.close()