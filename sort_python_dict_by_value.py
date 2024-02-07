# How to sort a Python dict by value
# (== get a representation sorted by value)

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

print(sorted(xs.items(), key=lambda x: x[1]))
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# Or:

import operator
print(sorted(xs.items(), key=operator.itemgetter(1)))
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]


# Reverse sort by keys:
my_dict = {'a': 3, 'b': 1, 'c': 2}

# Reverse sort by keys
sorted_dict_by_keys = dict(sorted(my_dict.items(), key=lambda x: x[0], reverse=True))

print(sorted_dict_by_keys)


# Reverse sort by values:
my_dict = {'a': 3, 'b': 1, 'c': 2}

# Reverse sort by values
sorted_dict_by_values = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))

print(sorted_dict_by_values)
