num = int(input("Enter a number: "))  # take input from user # 153, 371

# find the sum of the cubes of each digit
sum = 0
for digit in str(num):
    sum += int(digit) ** 3

# check if the given number is an Armstrong number or not
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
