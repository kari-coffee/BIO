# a) [25]
# b) 14, BIO, NTU, ABCDE, BIO14 [2]
# c) 68719476735
# d) [0] x 
# Answer:
# Two adjacent passwords are either the same length or 1 different
# The passwords must be both 18 characters, as 17+18 < 36 and 18+19 > 36
# The first password must start with A, and must be the last password of length 18
# starting with A, as A cannot be reused
# Last password starting with A with 18 letters is ATUV..789
# First password starting with B with 18 letters is BCDE...QRS

n = int(input())
alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
# build up dp table of lengths and letters
# each row is a length of password
# each col is a letter
dp = [[0 for i in range(36)] for j in range(36)]
# fill in 1s for length of 1
for i in range(36):
    dp[0][i] = 1
for i in range(1, 36):
    for j in range(36):
        dp[i][j] = sum(dp[i-1][j+1:])
# rows maps a length to the total number of passwords of that length
rows = {i:sum(dp[i]) for i in range(36)}
# find which length n belongs to
for i in range(36):
    if rows[i] >= n:
        length = i+1
        break
    else:
        n -= rows[i]
s = ''
for l in range(length-1, -1, -1):
    start = 0
    if s != '':
        start = alpha.index(s[-1])+1 # can only use letters alphabetically after
    for j in range(start, 36):
        if dp[l][j] >= n:
            s += alpha[j]
            break
        else:
            n -= dp[l][j]
print(s)

# c)
# total = 0
# for i in range(36):
#     for j in range(36):
#         total += dp[i][j]
# print(total)