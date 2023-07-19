# Filter even numbers from a list:

arr = [1, 2, 3, 4, 5, 6, 7, 8]
even = [i for i in arr if i % 2 == 0]
print(even)

# Convert strings to uppercase:

words = ['hello', 'world', 'python']
uppercase_words = [word.upper() for word in words]

# Use list comprehension with a conditional expression:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = ['even' if x % 2 == 0 else 'odd' for x in numbers]
