# List comprehension

a = [1,3,5,7,9,11]

# create a new list like == [2,6,10,14,18,22]
# basically doubling every element in the original list

# Solution 1
# create a new list

b = []

for x in a: 
    b.append(x*2)
    
print(b)

# Solution 2
# using list comprehension

c = [x * 2 for x in a]
print(c)

# If we want to create this list instead == [1,4,9,16,25,36]

# Solution 1 -- using append function

d1 = []
for x in range(1, 7):
    d1.append(x ** 2)

print(d1)

# Solution 2 -- using list comprehension
d2 = [x ** 2 for x in range(1,7)]
print(d2)

# Challenge --> create this list == [36, 25, 16, 9, 4, 1]

# Solution 1 -- using append function 
e1 = []

for x in range(6, 0, -1):
    e1.append(x ** 2)
    
print(e1)

# Solution 2 -- using list comprehension

e2 = [x ** 2 for x in range(6,0,-1)]
print(e2)


# Problem --> find the sum of unique elements from the givenList

given_list = [1,3,4,1,3]

# create a new set from this list, because it will fetch the unique elements only

s1 = set()

for x in given_list:
    s1.add(x)
print("New set from the given list: ", s1)

sum_unique = 0
for x in s1:
    sum_unique += x
    
print("Sum of unique elements=", sum_unique)