# dictionaries
# - key/value pairs
# like Javascript Object/Computer Science HashMap

my_dictionary = { "Pikachu": "Electricity", "Charmander": "Fire"}

my_ordinary_dictionary = dict(gasty="Dark", mrMime="Psychical")

# can be implemented as a list of tuples
my_wow_dictionary = dict([ ("Onix", "Rock"), ("Caterpie", "Grass") ])

# implementing or updating a value
my_dictionary["Snorlax"] = "Normal"

del(my_dictionary["Charmander"])

print(my_dictionary.pop('Pikachu'))

print(my_ordinary_dictionary.keys())
print(my_ordinary_dictionary.values())
print(my_ordinary_dictionary.items())

# iterating - remember it is a random order!
for key, value in my_ordinary_dictionary.items():
    print(key, value)