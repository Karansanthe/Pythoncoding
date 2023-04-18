arr = [3, 6, 1, 8, 4, 2, 9, 5]
n = len(arr)

if n < 2:
    print("The array should have at least two elements.")
else:
    # initialize the two pointers to the first two elements
    largest = max(arr[0], arr[1])
    second_largest = min(arr[0], arr[1])

    for i in range(2, n):
        # check if the current element is greater than the largest
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        # check if the current element is greater than the second largest
        elif arr[i] > second_largest:
            second_largest = arr[i]

    print(f"The second largest element in the array is {second_largest}.")


"""
#Second-largest element in an array using sorting:

arr = [3, 6, 1, 8, 4, 2, 9, 5]
arr.sort(reverse=True)
print(arr[1])
"""

"""
#using heapq

import heapq

arr = [3, 5, 2, 8, 1, 9, 4, 6]

largest_two = heapq.nlargest(2, arr)
second_largest = largest_two[1]

print(second_largest)"""