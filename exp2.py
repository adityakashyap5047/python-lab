# Write a python program to understand operation on string

my_str = "Hello World"
print(my_str)

# Accessing characters in a string
print(my_str[0])

# Accessing substrings
print(my_str[1:5])

# Accessing substrings with step
print(my_str[1:5:2])

# Accessing substrings without start index
print(my_str[:5])

# Accessing substrings without end index
print(my_str[1:])

# Accessing substrings without start and end index
print(my_str[:])

# concatenation
my_str1 = "Hello"
my_str2 = "World"
print(my_str1 + my_str2)

# Repetition
print(my_str1 * 3)

# Membership
print('H' in my_str1)

# Membership
print('H' not in my_str1)

# uppercase
print(my_str1.upper())

# lowercase
print(my_str1.lower())

# string length
print(len(my_str1))

# Write a python program to understand operation on list

my_list = [1, 2, 3, 4, 5]
print(my_list)

# length of a list
print(len(my_list))

# Accessing elements in a list
print(my_list[0])

# slicing in a list
print(my_list[1:3])

# slicing in a list
print(my_list[1:4:2])

# appending elements in a list
my_list.append(6)
print(my_list)

# removing elements in a list
my_list.remove(6)
print(my_list)

# count elements in a list
print(my_list.count(3))

# reverse elements in a list
my_list.reverse()
print(my_list)

# Write a python program to understand operation on tuple

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# length of a tuple
print(len(my_tuple))

# Accessing elements in a tuple
print(my_tuple[0])

# slicing in a tuple
print(my_tuple[1:3])

# slicing in a tuple
print(my_tuple[1:4:2])

# count elements in a tuple
print(my_tuple.count(3))

# reverse elements in a tuple
my_tuple = my_tuple[::-1]
print(my_tuple)


# Write a python program to understand operation on set

my_set = {1, 2, 3, 4, 5}
print(my_set)

# length of a set
print(len(my_set))

# Accessing elements in a set
# print(my_set[0]) # Error

# Adding elements in a set
my_set.add(6)

# Removing elements in a set
my_set.remove(6)

# Removing elements in a set
my_set.discard(6)

# Removing elements in a set
my_set.pop()

# Removing elements in a set
my_set.clear()

# Write a python program to understand operation on dictionary

my_dict = {1: 'one', 2: 'two', 3: 'three'}
print(my_dict)

# length of a dictionary
print(len(my_dict))

# Accessing elements in a dictionary
print(my_dict[1])

# Accessing elements in a dictionary
print(my_dict.get(1))

# Adding elements in a dictionary
my_dict[4] = 'four'
print(my_dict)

# Removing elements in a dictionary
del my_dict[4]
print(my_dict)

# Removing elements in a dictionary
my_dict.pop(2)
print(my_dict)