# Exercise 5
# More Variables and Printing 

name = "Cory Smith"
age = 28
height = (6 * 12) + 5 # inches
weight = 280
eyes = "Green"
teeth = "White"
hair = "Brown"

print(f"Lets talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually, thats pretty heavy.")
print(f"He's got {eyes} eyes and {hair} hair too.")
print(f"His teeth are usually {teeth} depending on the tea.")

# This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}")

# calculat KG for weight
weight_kg = 0.453 * weight
print(f"My weight in kilograms is {weight_kg}.")