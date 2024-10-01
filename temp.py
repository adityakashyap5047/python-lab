# Write a python program to take 5 numbers as input from user and store them in a tuple and then calculate the sum of number
li = []
for i in range(5):
    num = int(input(f"Enter {i+1}th number: "))
    li.append(num)
tup = tuple(li)
sum = 0
for i in tup:
    sum = sum + i
print(sum)