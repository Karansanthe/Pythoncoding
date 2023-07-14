decimal_number = 42
binary_number = bin(decimal_number)[2:]

print(binary_number)

binary_number = '101010'
decimal_number = int(binary_number, 2)

print(decimal_number)
binary_number = '101010'
decimal_number = int(binary_number, 2)

print(decimal_number)

# [2:] because if we not use it will print 0b101010 to remove 0b we use that