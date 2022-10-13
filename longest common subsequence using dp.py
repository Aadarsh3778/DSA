def lcs(seq1, seq2):
    n, m = len(seq1), len(seq2)
    table = [[0 for i in range(m + 1)] for i in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if seq1[i] == seq2[j]:
                table[i + 1][j + 1] = 1 + table[i][j]
            else:
                table[i + 1][j + 1] = max(table[i + 1][j], table[i][j + 1])
    return table[-1][-1]


str1 = "analogy"
str2 = "alchemy"
st1 = "longest"
st2 = "stone"
print(lcs(str1, str2))
print(lcs(st1, st2))
