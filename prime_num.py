def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

num = 7

if is_prime(num):
    print("yes")
else:
    print("no")


# To print 1 to n:

"""def is_prime(num):
    
    if num <= 1:
        return False
        
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for num in range(1, 25):
    if is_prime(num):
        print(num, end=" ")

"""