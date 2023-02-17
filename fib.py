n = int(input("Enter the value of n: "))  # get the value of n from the user
fib = [0, 1]  # initialize the first two terms of the sequence

if n < 2:
    print(*fib[:n], sep=', ')  # print the first n terms of the sequence
else:
    for i in range(2, n):
        next_fib = fib[i - 1] + fib[i - 2]  # calculate the next term in the sequence
        fib.append(next_fib)  # add the next term to the list
    print(*fib, sep=', ')  # print the entire sequence

"""
The * is used to unpack the fib list and print its contents as separate arguments to the print() function.
In other words, the * is used to "unpack" the list and pass its elements as separate arguments to the function.
"""
