# Without using a function, you can manually create a generator using a loop and the `yield` statement.

# Generator to yield even numbers from 1 to 10
def even_generator(max_value):
    num = 1
    while num <= max_value:
        if num % 2 == 0:
            yield num
        num += 1

# Using the generator in a loop
for num in even_generator(10):
    print(num)
# Output: 2, 4, 6, 8, 10
