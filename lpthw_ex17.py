# Exercise 17
# More Files 

from sys import argv
# import the "exists" fucntion from the OS module 
from os.path import exists

# unpack all of the command line parmeters and assign them to variables. 
script, from_file, to_file = argv

#print(f"Copying {from_file} to {to_file}")

#in_file =open(from_file)
#indata = in_file.read()

# Open the file, read the file and assign to a data varaible. - this automatically closes the file too
# no need to close the file at the end of the script. 
indata = (open(from_file)).read()

#print(f"The input file is {len(indata)} bytes long.")

#print(f"Does the output file exist? {exists(to_file)}")
#print("Ready, hit RETURN to continue, CTRL-C to abort.")

#input()

# open the target file for writing
out_file = open(to_file, 'w')
# Write the input data to the target file. 
out_file.write(indata)

#print("Alright, all done.")
# close the target file. 
out_file.close
#in_file.close