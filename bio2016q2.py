# a) [24]
# b) 16 [2]
# c) example input: 1 3 8, 2 18 20
#    20 ways [4]
# d) No, as you don't know if migration happened at the location where the person 
# was added. If the location where the person was added has value more than 0, 
# it is possible for both migration to not, and to have happened, to have led 
# to that ending landscape. For example, if migration didn't happen, the person 
# will have just been placed there, and the location's value incremented by 1
# However, the location could have had value 3 and adding the person would have 
# caused migration, and eventually led to the same ending landscape [4]

from collections import defaultdict
p, s, n = [int(i) for i in input().split()]
p -= 1
seq = [int(i) for i in input().split()]
i = 0
landscape = defaultdict(lambda: 0)
def find_start(start_x, start_y, v):
    start_x = start_x+(v%5)
    if start_x >= 5:
        start_y += start_x//5
    start_x %= 5
    start_y = (start_y+(v//5))%5
    return (start_x, start_y)
overcrowded = []
def migrate(x, y):
    landscape[(x, y)] -= 4
    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        landscape[(x+dx, y+dy)] += 1
        if landscape[(x+dx, y+dy)] >= 4 and (x+dx, y+dy) not in overcrowded:
            overcrowded.append((x+dx, y+dy))

start_x, start_y = find_start(0, 0, p)
landscape[(start_x, start_y)] += 1
for step in range(1, n):
    start_x, start_y = find_start(start_x, start_y, seq[i])
    i = (i+1)%len(seq)
    landscape[(start_x, start_y)] += 1
    if landscape[(start_x, start_y)] >= 4 and (start_x, start_y) not in overcrowded:
        overcrowded.append((start_x, start_y))
    while overcrowded:
        cur_x, cur_y = overcrowded.pop(0)
        migrate(cur_x, cur_y)
        if landscape[cur_x, cur_y] >= 4:
            overcrowded.append((cur_x, cur_y))

for i in range(5):
    row = []
    for j in range(5):
        row.append(landscape[(j,i)])
    print(*row)

# code for part c) 
# from collections import defaultdict
# res = """1 0 1 0 0
# 1 0 1 0 0
# 1 0 0 0 0
# 1 0 1 0 0
# 1 0 0 0 0"""
# ans = 0
# target = [[int(i) for i in i.split()] for i in res.split('\n')]
# for p in range(25):
#     for a in range(25):
#         for b in range(25):
#             for c in range(25):
#                 s, n = 3, 8
#                 seq = [a, b, c]
#                 i = 0
#                 landscape = defaultdict(lambda: 0)
#                 def find_start(start_x, start_y, v):
#                     start_x = start_x+(v%5)
#                     if start_x >= 5:
#                         start_y += start_x//5
#                     start_x %= 5
#                     start_y = (start_y+(v//5))%5
#                     return (start_x, start_y)
#                 overcrowded = []
#                 def migrate(x, y):
#                     landscape[(x, y)] -= 4
#                     for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
#                         landscape[(x+dx, y+dy)] += 1
#                         if landscape[(x+dx, y+dy)] >= 4 and (x+dx, y+dy) not in overcrowded:
#                             overcrowded.append((x+dx, y+dy))
#                 start_x, start_y = find_start(0, 0, p)
#                 landscape[(start_x, start_y)] += 1
#                 for step in range(1, n):
#                     start_x, start_y = find_start(start_x, start_y, seq[i])
#                     i = (i+1)%len(seq)
#                     landscape[(start_x, start_y)] += 1
#                     if landscape[(start_x, start_y)] >= 4 and (start_x, start_y) not in overcrowded:
#                         overcrowded.append((start_x, start_y))
#                     while overcrowded:
#                         cur_x, cur_y = overcrowded.pop(0)
#                         migrate(cur_x, cur_y)
#                         if landscape[cur_x, cur_y] >= 4:
#                             overcrowded.append((cur_x, cur_y))
                
#                 arr = []
#                 for i in range(5):
#                     row = []
#                     for j in range(5):
#                         row.append(landscape[(j,i)])
#                     arr.append(row)
#                 if arr == target:
#                     ans += 1
#                     print(p, 3, 8)
#                     print(a, b, c)
# print(ans)