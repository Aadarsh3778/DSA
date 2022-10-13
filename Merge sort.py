"""
### Merge Sort ###
- Uses the concept of divide and conquer.
- first takes the mid-index of a list and divide them.
- this process continues unless we have a single elements at the end.
- then it starts comparing the elements and placing into ascending order in left and right list.
- at the end merge function will merge.
- merge will take left and right list and will compare elements and will return the merged and sorted list.


- for eg:-
[38, 27, 43, 3, 9, 82, 10]
getting the mid-index lets say 3 and dividing into left and right.
    left                 right
[38, 27, 42, 3]       [9, 82, 10]
[38, 27] [42, 3]      [9] [82, 10]
[38] [27] [42] [3]    [9] [82] [10]

- now sorting by comparing(using merge function).
[38] [27] [42] [3]    [9] [82] [10]
[27, 38] [3, 42]      [9] [10, 82]
[3, 27, 38, 42]       [9, 10, 82]

- final result
[3, 9, 10, 27, 38, 42, 82]

- Time Complexity:- O(nLogn)
- Space Complexity:- O(n)

"""


def merge(nums1, nums2):
    # List to store the results
    merged = []

    # Indices for iteration
    i, j = 0, 0

    # Loop over the two lists
    while i < len(nums1) and j < len(nums2):

        # Include the smaller element in the result and move to next element
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Get the remaining parts
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]

    # Return the final merged array
    return merged + nums1_tail + nums2_tail


def merge_sort(nums):
    # Terminating condition (list of 0 or 1 elements)
    if len(nums) <= 1:
        return nums

    # Get the midpoint
    mid = len(nums) // 2

    # Split the list into two halves
    left = nums[:mid]
    right = nums[mid:]

    # Solve the problem for each half recursively
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    # Combine the results of the two halves
    sorted_nums = merge(left_sorted, right_sorted)

    return sorted_nums


print(merge_sort([5, 9, 8, 7, 1, 2, 4, 3, 45]))

"""
# not the right way to merge two list.
def merge(left_lst, right_lst):
    l = []

    for i in left_lst:
        for j in right_lst:
            if j < i:
                l.append(j)
        l.append(i)

    return list(set(l))

print(merge([1,4,7,9,11], [0,2,3,8,12]))
"""

"""
# Error
def merge(left_lst, right_lst):
    merged = []
    i, j = 0, 0

    while i < len(left_lst) and j < len(right_lst):
        if left_lst[i] <= right_lst[i]:
            merged.append(left_lst[i])
            i += 1
        else:
            merged.append(right_lst(j))
            j += 1

    left_last = left_lst[i:]
    right_last = right_lst[j:]

    return merged + left_last + right_last

print(merge([1, 4, 7, 9, 11], [-1, 0, 2, 3, 8, 12]))

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2

    left = lst[:mid]
    right = lst[mid:]

    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    sorted_merge = merge(left_sorted, right_sorted)

    return sorted_merge

print(merge_sort([5,9,8,7,1,2,4,3,45]))
"""
