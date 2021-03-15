# sets #
#  - it is unordered
#  - store non duplicate values

a = set([1,2,3])
b = { 7,2,5 }
x = [5,4,3]
c = set(x)
print(a,b,c)

a.add(4) # .add instead of .append

a.pop() # pop a random item

a.discard(2) # remove an element from a set if it is a member

3 in a # check membership

# on set, the mathematical operations are better

print("set a: ",a ,"set c: ", c) # set a:  {2, 3, 4} set c:  {3, 4, 5}
print(a & c) # {3, 4}
print(a | c) # {2, 3, 4, 5}
print(a ^ c) # {2, 5} - what is not common in both sets
print(a - c) # {2} - what is in a but not in c
print(a >= c) # False - if a contains c
print(a <= c) # False - if c contains a