"""
### Bubble Sort ###
- We swap the elements here takin 1st and 2nd element and swap if 2nd is greater and so on.
- Time complexity:- O(n^2).
"""


def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                # print(i, j, lst)
    return lst


print(bubble_sort([1, 2, 3]))
