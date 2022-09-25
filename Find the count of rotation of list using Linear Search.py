"""
Q: Find the count that how many times was the sorted list rotated.
"""


def findCount(arr):
    position = 0
    while position < len(arr):
        if arr[position] < arr[position - 1]:
            ans = position
            if ans > 0:
                return ans

        position += 1
    return -1


"""
# Method 2:- 
def findCount(arr):
    for i in range(len(arr)):
        if arr[i] < arr[i-1]:
            ans = arr.index(arr[i])
            if ans > 0:
                return ans
    return -1

"""

lst = [5, 6, 7, 1, 2, 3, 4]

print(Find(lst))
print(Find([9, 8, 7, 6, 5, 4]))
print(Find([1, 2, 3, 4, 5, 6]))
