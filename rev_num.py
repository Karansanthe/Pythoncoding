num = int(input("Enter a number: "))  # get the input number from the user
reverse = 0

while num > 0:
    remainder = num % 10  # find the last digit of the number
    reverse = (reverse * 10) + remainder  # append the last digit to the reverse number
    num = num // 10  # remove the last digit from the number

print("The reversed number is:", reverse)
