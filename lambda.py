# Lambda functions are commonly used when you need a small function for a short period of time, 
# and you don't want to define a separate function using the def keyword.

# syntax: lambda arguments: expression

sum = lambda x, y: x + y
print(sum(3, 5))  # Output: 8

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]


# Compared with def fun

# Example 1: A simple function that adds two numbers using def keyword:

def add_numbers(x, y):
    return x + y


result = add_numbers(3, 5)
print(result)  # Output: 8

# Example 2: The same function using a lambda function:

add_numbers = lambda x, y: x + y

result = add_numbers(3, 5)
print(result)  # Output: 8


# Example 3: A function that uses an if statement to check whether a number is even or odd using def keyword:

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


result = is_even(4)
print(result)  # Output: True

# Example 4: The same function using a lambda function:

is_even = lambda x: True if x % 2 == 0 else False

result = is_even(4)
print(result)  # Output: True
