"""
### Binary Search ###
- Search for the mid-number than match if number is equal to the mid-number or not.
- if yes than ans is mid-number.
- if not than check if the mid-number is higher or smaller than the num.
- if smaller or greater than sift to accordingly the mid and repeat from step1.
- complexity : O(log n).
"""


def findNumber(arr, num):
    arr = sorted(arr)
    l, h = 0, len(arr) - 1
    while l <= h:
        mid = (l + h) // 2
        mid_number = arr[mid]
        if mid_number == num:
            return mid
        elif num < mid_number:
            h = mid - 1
        elif num > mid_number:
            l = mid + 1
    return -1


lst = [1, 2, 4, 5, 3, 7, 8, 9, 4, 5]
n = 7
print(f"Test 1: {sorted(lst)}: Position for {n}: ", findNumber(lst, n))
print(f"Test 2: {sorted([9, 8, 7, 6, 5, 2, 3, 4, 1])}: Position for {4}: ", findNumber([9, 8, 7, 6, 5, 2, 3, 4, 1], 4))
