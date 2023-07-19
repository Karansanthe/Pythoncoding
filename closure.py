def outer_function(x):
    # This is the outer function that contains the inner function
    def inner_function(y):
        # The inner function can use 'x' from the outer function
        return x + y
    return inner_function

# Create a closure by calling the outer function with an argument
closure_function = outer_function(10)

# Call the closure function
result = closure_function(5)
print(result)  # Output: 15
