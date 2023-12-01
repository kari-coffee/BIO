from collections import deque
target = input()
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:len(target)]

done = set()
queue = deque([['', 0]]) #display, warehouse, swapped?
while queue:
    display, c = queue.popleft()
    if display == target:
        print(c)
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

# b)
# from itertools import permutations
# for i in permutations('ABCDE'):
#     target = ''.join(i)
#     s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:len(target)]

#     done = set()
#     queue = [['', s, 0, 0]] #display, warehouse, swapped?
#     while queue:
#         display, warehouse, swapped, c = queue.pop(0)
#         if display == target:
#             #print(c)
#             break
#         c += 1
#         #add
#         if len(warehouse) != 0:
#             x = (display+warehouse[0], warehouse[1:], 0, c)
#             if x[0] not in done:
#                 done.add(x[0])
#                 queue.append(x)
#         #swap
#         if not swapped and len(display) >= 2:
#             x = (display[:2][::-1]+display[2:], warehouse, 1, c)
#             if x[0] not in done:
#                 done.add(x[0])
#                 queue.append(x)
#         #rotate
#         if len(display) > 2:
#             x = [display[1:]+display[0], warehouse, 0, c]
#             if x[0] not in done:
#                 done.add(x[0])
#                 queue.append(x)
#     if c == 6:
#         print(target)

# # c)
# target = input()
# s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:len(target)]

# done = set()
# queue = [['', s, 0]] #display, warehouse, swapped?
# ans = 0
# while queue:
#     display, warehouse, c = queue.pop(0)
#     if c > 24:
#         continue
#     if display == target:
#         if c == 24:
#             ans += 1
#         continue
#     c += 1
#     #add
#     if len(warehouse) != 0:
#         x = (display+warehouse[0], warehouse[1:], c)
#         if x not in done:
#             done.add(x)
#             queue.append(x)
            
#     #swap
#     if len(display) >= 2:
#         x = (display[:2][::-1]+display[2:], warehouse, c)
#         if x not in done:
#             done.add(x)
#             queue.append(x)
#     #rotate
#     if len(display) > 2:
#         x = (display[1:]+display[0], warehouse, c)
#         if x not in done:
#             done.add(x)
#             queue.append(x)
# print(ans)