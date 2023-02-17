num = 28  # replace with the number you want to check
# 6, 28, 496, 8128, 33,550,336, 8,589,869,056
sum_divisors = 0
for i in range(1, num):
    if num % i == 0:
        sum_divisors += i

if sum_divisors == num:
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")
