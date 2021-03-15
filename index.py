# indexing #
x = "crazyfrog"
print(x)
print(x[2])
print(x[5:7])
print(x[1:6])
print(x[5:])
print(x[:5])
print(x[-5])
print(x[:-4])

# multipying a sequence
mytuple = (1,2,3,4,5,6)
print(mytuple * 3)

print('bonjour ' * 5 )

# in or not in
print('r' in x)
print('k' not in x)

# iterating
for item in mytuple:
    print("mytuple item: " + str(item))

for index, item in enumerate(mytuple):
    print("[" + str(index)+ "]" +  ": " + str(item))

print(min(mytuple))
print(max(mytuple))
print(sum(mytuple))

myarray = [5,7,2,8,1,5,3,4,2]

print(sorted(myarray))

print("count of r's in x variable: " + str(x.count('r')))

# destructurization

myarraysecond = ["Pikachu", "Bulbassaur", "Squirtle"]
pikachu, bulbassaur, squirtle = myarraysecond
print(pikachu)

# generating arrays

generatedarray = [ i for i in range(10)]
print(generatedarray)

complicated_generated_array = [ i**2 for i in range(10) if i > 2]
print(complicated_generated_array)