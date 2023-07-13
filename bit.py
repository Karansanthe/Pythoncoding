n = 4
k = 2
print(n | (1 << (k - 1))) # Set
print(n & (~(1 << (k - 1)))) # Clear
print(n ^ (1 << (k - 1))) # Toggle
