num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial of", num, "is", factorial)


"""

# find the factorial of a given number without using if-else, for, and ternary operators:

num = int(input("Enter a number: "))
result = 1
while num:
    result *= num
    num -= 1
print(result)
"""
