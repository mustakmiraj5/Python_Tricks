# Shortest array length 
string_array = ["apple", "banana", "kiwi", "orange"]

# Using the min function with a lambda function as the key
shortest_length = min(string_array, key=lambda s: len(s))

print("Shortest length of string:", len(shortest_length))

# Shortest string 
strings = ["some", "example", "words", "that", "i", "am", "fond", "of"]

print (min(strings, key=len)) # prints "i"
