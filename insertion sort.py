"""
### Insertion Sort ###
- Slightly better than bubble sort.
- In bubble sort we swap but in insertion sort we actually sift.

for eg:-
[5, 2, 8, 7, 9, 4]
- here we keep 5 as a sorted element and start checking from second element.
- we check if the 2nd element is greater or smaller.
- if greater than we will leave as it is.
- if smaller than we will sift 2nd element before the first element and so on.

- Time Complexity:- O(n^2).
"""


def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i - 1
        while j >= 0 and nums[j] > cur:
            j -= 1
        nums.insert(j + 1, cur)
    return nums
 

print(insertion_sort([5, 7, 9, 8, 4, 2, 1]))
