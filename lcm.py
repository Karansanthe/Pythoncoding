n1 = 4
n2 = 6

max_num = max(n1, n2)
lcm = max_num

while True:
    if lcm % n1 == 0 and lcm % n2 == 0:
        break
    lcm += max_num
print(lcm)
