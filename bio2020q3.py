# a) [27]
# b) 39,29947 [3]
# c) p is odd, as the plan must be in the middle, 
# and for there to be a middle plan, there must be an odd number of plans. [3/5]
p, rep, r = [int(i) for i in input().split()]
n = int(input())
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:p]

memo = {}
def ways(letter, q, r):
    if r == 1:
        return 1
    elif (letter, q, r) in memo:
        return memo[(letter, q, r)]
    res = 0
    for new in alpha:
        if new == letter:
            if q == 1:
                continue
            res += ways(new, q-1, r-1)
        else:
            res += ways(new, rep, r-1)
    memo[(letter, q, r)] = res
    return res
ans = ''
def count_rep(cur, letter):
    res = 0
    for i in cur[::-1]:
        if i == letter:
            res += 1
        else:
            break
    return res
    
for i in range(r):
    for letter in alpha:
        if count_rep(ans, letter) == rep:
            continue
        if (x := ways(letter, max(1, rep-count_rep(ans, letter)), r-i)) >= n:
            ans += letter
            break
        else:
            n -= x
print(ans)

#b)
# p = 4
# rep = 2
# r = 8
# alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:p]
# res = ''
# c = 0
# while res != 'CCABABCC':
#     c += 1
#     n = c
#     res = ''
#     for i in range(r):
#         for letter in alpha:
#             if count_rep(res, letter) == rep:
#                 continue
#             if (x := ways(letter, max(1, rep-count_rep(res, letter)), r-i)) >= n:
#                 res += letter
#                 break
#             else:
#                 n -= x
# print(c)