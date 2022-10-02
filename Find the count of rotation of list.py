"""
Q: Find the count that how many times was the sorted list rotated.
"""


def findCount(arr):
    sorted_arr = sorted(arr)
    count = 0
    for i in range(len(arr)):
        if arr[i] == sorted_arr[0]:
            return count
        count += 1
    return -1


lst = [5, 6, 7, 1, 2, 3, 4]

print(f"Test1: Arr: {lst}, Output: {findCount(lst)}, Expected Output: {3}")
print(f"Test2: Arr: {[9, 8, 7, 6, 5, 4]}, Output: {findCount([9, 8, 7, 6, 5, 4])}, Expected Output: {5}")
print(f"Test3: Arr: {[1, 2, 3, 4, 5, 6]}, Output: {findCount([1, 2, 3, 4, 5, 6])}, Expected Output: {-1}")