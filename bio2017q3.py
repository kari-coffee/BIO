# a) [22/25] (runs too slowly for 2 9 17 24 input)
# b) 17? [0/2] ms says 18... (i just ran code with inputs 3 3 6 n and summed them up)
# c) I'm not doing this... this is like an entire part a) again
from collections import Counter
p, i, n, w = [int(i) for i in input().split()]
# p = number of parcels
# i = item weight limit
# n = total number of items in a distribution
# w = weight of each parcel

# partitions?
cap = n+1-(p-1)
dp = [[0 for x in range(w+1)] for y in range(cap)]
used = [[[] for x in range(w+1)] for y in range(cap)]
def count(c):
    arr = []
    for i in c:
        for j in range(c[i]):
            arr.append(i)
    return arr
for ix in range(1, i+1):
    dp[1][ix] = 1
    used[1][ix].append(Counter([ix]))
for items in range(1, cap):
    for weight in range(1, w+1):
        for wi in range(1, i+1):
            if wi <= weight:
                for prev_took in used[items-1][weight-wi]:
                    taken = Counter([wi]+count(prev_took))
                    if taken not in used[items][weight]:
                        dp[items][weight] += 1
                        used[items][weight].append(taken)

for weight in range(1, w+1):
    dp[0][weight] = 1
memo = {}
def construct(left, taken):
    l = sum(taken)
    if left == 0 and l == n:
        return 1
    elif left == 0:
        return 0
    elif (left, l) in memo:
        return memo[(left, l)]
    ans = 0
    for parcel_length in range(1, cap):
        if l+parcel_length <= n:
            ans += dp[parcel_length][w]*construct(left-1, taken+[parcel_length])
    memo[(left, l)] = ans
    return ans

print(construct(p, []))