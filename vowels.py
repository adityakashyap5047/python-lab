# Write a python program to counts the vowel in given string

my_str = input("Enter a string: ")

count = 0

for i in my_str:
    if i.lower() in "aeiou":
        count += 1

print(f"Number of vowels in the string: {count}")