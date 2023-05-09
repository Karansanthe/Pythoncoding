arr = [28, 43, 26, 65, 37, 66, 62, 59]

n = len(arr)

if n < 2:
    print("The array should have at least two elements.")
else:
    largest = second_largest = -float('inf')

    for i in range(n):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]

    if second_largest == -float('inf'):
        print("There is no second largest element.")
    else:
        print(f"The second largest element in the array is {second_largest}.")
