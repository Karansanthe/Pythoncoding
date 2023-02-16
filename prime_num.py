# Python program to display prime numbers till N

N = 20
# check for every number from 2 to N
for i in range(2, N + 1):
    # assume number is prime unless proven otherwise
    is_prime = True
    # check if current number is prime
    # for j in range(2, int(i/2)+1):
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=" ")
