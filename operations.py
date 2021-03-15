import random

phrase = "I have only 8 pokeballs left and there are so many pokemons! 3 Onixes and 12 Pikachu's"
print( [ n for n in phrase if n.isnumeric()]) # ['8', '3', '1', '2']

# shuffling
my_array = [x for x in range(10)]
random.shuffle(my_array)
print(my_array)