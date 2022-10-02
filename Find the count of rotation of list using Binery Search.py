"""
Q: Find the count that how many times was the sorted list rotated.
- Using Binary Search
"""


def findCount(arr, num):
    l = 0
    h = len(arr) - 1
    for i in range(len(arr)):
        mid = (l + h) // 2
        if mid == num:
            return mid

        elif num > mid:
            l = mid + 1

        else:
            h = mid - 1


def evaluation():
    red = '\033[91m'
    green = '\033[92m'
    en = '\033[0m'
    d = [{"arr": [5, 6, 7, 1, 2, 3, 4], "query": 3},
         {"arr": [4, 5, 6, 7, 8, 1, 2, 3], "query": 5},
         {"arr": [1, 2, 3, 4, 5], "query": -1},
         {"arr": [9, 8, 7, 6, 5], "query": 5}]
    for i in d:
        a = i["arr"]
        q = i["query"]
        ans = findCount(a, q)
        if ans == q:
            result = f"{green} Passed {en}"

        else:
            result = f"{red} Fail {en}"

        print(f"Test Case:-- {result}\nArray: {a}\nExpected Output: {q}\nActual Output: {ans}")
        print("-" * 30)


evaluation()


"""
from TestCase_oops import TestCase

a = TestCase()
b1 = a.case([5, 6, 1, 2, 3, 4], 3)
b2 = a.case([4, 5, 6, 7, 8, 1, 2, 3], 5)
b3 = a.case([1, 2, 3, 4, 5], -1)
b4 = a.case([9, 8, 7, 6, 5], 5)

c = a.list_of_cases(b1, b2, b3, b4)
for i in c:
    m = findCount(i["arr"], i["query"])
    a.evaluation(i, m)
"""
