# a) [24]
a, b = input().split()

def is_pat(s):
    if len(s) == 1:
        return True
    for i in range(1, len(s)):
        c, d = s[:i], s[i:]
        #if sorted(list(c))[0] > sorted(list(d))[-1]:
        if min(c) > max(d):
            if is_pat(c[::-1]) and is_pat(d[::-1]):
                return True
    return False

for s in [a, b, a+b]:
    if is_pat(s):
        print('YES')
    else:
        print('NO')

# # b)
# from itertools import permutations
# c = 0
# for s in permutations('ABCD', 4):
#     s = ''.join(s)
#     if is_pat(s):
#         print(s)
#         c += 1
# print(c)

# # c)
# from itertools import permutations
# alpha = 'ACDEFGHIJKLMNOPQRSTUVWXYZ'
# c = 0
# for i in permutations(alpha):
#     s = 'B' + ''.join(i)
#     if is_pat(s):
#         c += 1
# print(c)
