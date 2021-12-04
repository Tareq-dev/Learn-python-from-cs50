# x = int(input("x: "))
# y = int(input("y: "))

# result = x / y
# print(f"{x} / {y} {result}")

# here exception means when we devided a number by zero then we got a weird error which
# we shouldnt show the website.


import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error:Invalid Input.")
    sys.exit(1)
try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} {result}")
