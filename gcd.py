#HCF
a = 24
b = 36

while b != 0:
    a, b = b, a % b

print("The GCD of 24 and 36 is:", a)
    