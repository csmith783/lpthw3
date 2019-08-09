# Exercise 39
# Dictionaries, Oh Lovely Dictionaries 

# Create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California:': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# Create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'    
}

# Add some more cities 
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print out some cities
print('-' * 10)
print('NY state has: ', cities['NY'])
print("OR state has: ", cities['OR'])

print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# Do it by using the states then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every states abbreviation 
print ('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state}'s abbreviaiton is {abbrev}.")

# print every cite in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{city} is in {abbrev}.")

# Now do both at the same time 
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated with {abbrev}.")
    print(f"{state} has the city {cities[abbrev]}.")

# safely get an abbreviation by state that might not be there 
print('-' * 10)
#state = states.get('Texas')

if not states.get('Texas'):
    print("Sorry, no Texas")

# get a city with a default value 
city = cities.get('TX', 'Does not exist.')
print(f"The city for the state 'TX' is: {city}.")

