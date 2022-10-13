"""
### The Longest Common Subsequence ###
- need to find the longest common subsequence.
for eg:-
analogy
alchemy

a, l, y are the only common so result is 3.

"""


def lsc(s1, s2, idx1=0, idx2=0):
    if idx1 == len(s1) or idx2 == len(s2):
        return 0
    elif s1[idx1] == s2[idx2]:
        return 1 + lsc(s1, s2, idx1 + 1, idx2 + 1)
    else:
        option1 = lsc(s1, s2, idx1 + 1, idx2)
        option2 = lsc(s1, s2, idx1, idx2 + 1)
        return max(option1, option2)


str1 = "analogy"
str2 = "alchemy"
st1 = "longest"
st2 = "stone"
print(lsc(str1, str2))
print(lsc(st1, st2))
