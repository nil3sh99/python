# to create a new dict 
d1 = {}
d2 = dict()
d3 = {
    "George": 24, 
    "Tom": 32
}

# to add a key-value pair
d1["George"] = 24
d1["Tom"] = 25
d1["Nilesh"] = 25

print(d1["George"])

# change the value associated with the key
d1["Nilesh"] = 26

print(d1["Nilesh"])

# Keys are most commonly strings or numbers

# Iterate over key value pairs

print("----------Iterating - METHOD 1------------")
# METHOD 1
for x in d1: 
    print(d1[x])
    
print("----------Iterating - METHOD 2------------")

for key, value in d1.items():
    print("Key:", end= " ")
    print(key)
    print("Value:", end= " ")
    print(value)