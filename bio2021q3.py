# a) [24]
# b) BACDE, BCADE, BCDAE, BCDEA [3]
# c) [0] (84)
from collections import deque
target = input()
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:len(target)]

done = set()
queue = deque([['', 0]])
while queue:
    display, c = queue.popleft()
    if display == target:
        break
    c += 1
    #add
    warehouse = s[len(display):]
    if len(warehouse) != 0:
        x = (display+warehouse[0], c)
        if x[0] not in done:
            done.add(x[0])
            queue.append(x)
    #swap
    if len(display) >= 2:
        x = (display[:2][::-1]+display[2:], c)
        if x[0] not in done:
            done.add(x[0])
            queue.append(x)
    #rotate
        x = (display[1:]+display[0], c)
        if x[0] not in done:
            done.add(x[0])
            queue.append(x)
print(c)

# # c) (gives 82, not 84?)
# from collections import deque
# target = input()
# s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:len(target)]

# done = set()
# parent = {}
# queue = deque([['', 0]])
# while queue:
#     display, c = queue.popleft()
#     if c > 30:
#         continue
#     c += 1
#     #add
#     warehouse = s[len(display):]
#     if len(warehouse) != 0:
#         x = (display+warehouse[0], c)
#         if x[0] not in done:
#             done.add(x[0])
#             queue.append(x)
#             if display in parent:
#                 parent[display].append(x[0])
#             else:
#                 parent[display] = [x[0]]
#     #swap
#     if len(display) >= 2:
#         x = (display[:2][::-1]+display[2:], c)
#         if x[0] not in done:
#             done.add(x[0])
#             queue.append(x)
#             if display in parent:
#                 parent[display].append(x[0])
#             else:
#                 parent[display] = [x[0]]
#     #rotate
#         x = (display[1:]+display[0], c)
#         if x[0] not in done:
#             done.add(x[0])
#             queue.append(x)
#             if display in parent:
#                 parent[display].append(x[0])
#             else:
#                 parent[display] = [x[0]]

# def ways(state):
#     res = 0
#     if state in parent:
#         for i in parent[state]:
#             res += ways(i)
#     else:
#         res = 1
#     return res
# print(ways(s))