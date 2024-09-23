# W.A.P to understand python keywords, identation and comments

# number = 10

# for i in range(1, number):
#     print(i)
#     if i % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# W.A.P to understand arithmetic operator

# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# op = input("Enter operator: ")

# if(op == '+'):
#     print(f"sum of {num1} and {num2} is {num1 + num2}")
# elif(op == '-'):
#     print(f"Difference of {num1} and {num2} is {num1 - num2}")
# elif(op == '*'):
#     print(f"Product of {num1} and {num2} is {num1 * num2}")
# elif(op == '/'):
#     print(f"Division of {num1} and {num2} is {num1 / num2}")
# elif(op == '%'):
#     print(f"Modulus of {num1} and {num2} is {num1 % num2}")
# else:
#     print("Invalid operator")

# W.A.P to understand bitwise operator

# Take two integer inputs from the user
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# Bitwise AND
# print(f"Bitwise AND of {num1} and {num2} is {num1 & num2}")

# Bitwise OR
# print(f"Bitwise OR of {num1} and {num2} is {num1 | num2}")

# Bitwise XOR
# print(f"Bitwise XOR of {num1} and {num2} is {num1 ^ num2}")

# Bitwise NOT
# print(f"Bitwise NOT of {num1} is {~num1}")
# print(f"Bitwise NOT of {num2} is {~num2}")

# Left Shift
# shift = int(input("Enter number of positions to shift left: "))
# print(f"{num1} left shifted by {shift} positions is {num1 << shift}")
# print(f"{num2} left shifted by {shift} positions is {num2 << shift}")

# Right Shift
# shift = int(input("Enter number of positions to shift right: "))
# print(f"{num1} right shifted by {shift} positions is {num1 >> shift}")
# print(f"{num2} right shifted by {shift} positions is {num2 >> shift}")

# W.A.P to understand assignment operator
count = int(input("Enter a number: "))
count += 1
print(f"count = {count}")
count -= 1
print(f"count = {count}")
count *= 2
print(f"count = {count}")
count /= 2
print(f"count = {count}")
count //= 2
print(f"count = {count}")
count **= 2
print(f"count = {count}")
count %= 3
print(f"count = {count}")

#W.A.P that takes 3 numbers as input from the user and perform following operations on three numbers multiplication, substraction and addition