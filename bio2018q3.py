# a) [24]
# b) 7, 16 [4]
# c) 26 [3/6] 2620
n = int(input())
s = input()
queue = [(s, 0)]
ans = 0
done = set()
done.add(s)
while queue:
    cur, dist = queue.pop(0)
    ans = max(ans, dist)
    for i in range(len(cur)-1):
        a, b = cur[i], cur[i+1]
        lo = min(int(a), int(b))
        hi = max(int(a), int(b))
        valid = False
        if i-1 >= 0:
            if lo < int(cur[i-1]) < hi:
                valid = True
        if i+2 < len(cur):
            if lo < int(cur[i+2]) < hi:
                valid = True
        if valid:
            new = cur[:i]+b+a+cur[i+2:]
            if new not in done:
                queue.append((new, dist+1))
                done.add(new)
print(ans)

# c) (doing 9 digits is too slow i hate python now)
# from itertools import permutations
# equiv = {}
# for s in list(permutations('12345')):
#     s = ''.join(s)
#     queue = [(s, 0)]
#     done = set()
#     equiv[s] = []
#     done.add(s)
#     while queue:
#         cur, dist = queue.pop(0)
#         if cur != s:
#             equiv[s].append(cur)
#         for i in range(len(cur)-1):
#             a, b = cur[i], cur[i+1]
#             lo = min(int(a), int(b))
#             hi = max(int(a), int(b))
#             valid = False
#             if i-1 >= 0:
#                 if lo < int(cur[i-1]) < hi:
#                     valid = True
#             if i+2 < len(cur):
#                 if lo < int(cur[i+2]) < hi:
#                     valid = True
#             if valid:
#                 new = cur[:i]+b+a+cur[i+2:]
#                 if new not in done:
#                     queue.append((new, dist+1))
#                     done.add(new)

# seen = set()
# d = {}
# c = 0
# for s in equiv:
#     if s not in seen:
#         c += 1
#     for check in equiv[s]:
#         if s != check and check not in seen:
#             seen.add(check)
# print(c)