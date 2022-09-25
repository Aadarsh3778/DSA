"""
### Linear Search ###
Complexity: O(N)

"""


def findNumber(arr, num):
    arr = sorted(arr)
    position = 0
    for i in arr:
        if i == num:
            return position
        position = position + 1

    return position


print("Test Case1: ", findNumber([1, 2, 4, 5, 3, 7, 8, 9, 4, 5], 7))
print("Test Case2: ", findNumber([9, 5, 4, 7, 6, 2, 1, 35], 4))