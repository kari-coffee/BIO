# a) [24]
# b) 23 [2]
# c) 8460 [0] x 9274
# d) They are on the edge of the board, as if every other set of dots 
# are joined, it is impossible to join two dots not on the edge without
# completing 2 squares. [3]

p1, m1, p2, m2, n = [int(i) for i in input().split()]

class dot():
    def __init__(self) -> None:
        self.d = {(0, -1):False, (1,0):False, (0,1):False, (-1,0):False}
dots = [[dot() for i in range(6)] for j in range(6)]
grid = [["*" for _ in range(5)] for x in range(5)]

def move(player, p, m):
    p += m
    if p >= 37:
        p -= 36
    dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    if player == 1:
        dir = [dir[0]] + dir[1:][::-1]
    
    placed = False
    while True:
        x = (p-1)%6
        y = (p-1)//6
        for dx, dy in dir:
            nx, ny = x+dx, y+dy
            if 0 <= nx <= 5 and 0 <= ny <= 5:
                if not dots[y][x].d[(dx,dy)]:
                    dots[y][x].d[(dx,dy)] = True
                    dots[ny][nx].d[(-dx, -dy)] = True
                    placed = True
                    break
        if placed:
            break
        p += 1
        if p >= 37:
            p = 1
    return p

def check(p):
    c = 0
    for y in range(5):
        for x in range(5):
            if grid[y][x] == "*":
                if dots[y][x].d[(1,0)] and dots[y][x].d[(0,1)] and dots[y+1][x+1].d[(-1,0)] and dots[y+1][x+1].d[(0,-1)]:
                    grid[y][x] = p
                    c += 1
    return c
first = 0
second = 0
turn = 0
for _ in range(n):
    if _ == 25:
        print()
    if turn == 0: #player 1
        p1 = move(0, p1, m1)
        won = check("X")
        first += won
        if won == 0:
            turn = 1

    else: #player 2
        p2 = move(1, p2, m2)
        won = check("O")
        second += won
        if won == 0:
            turn = 0

for row in grid:
    print(*row)
print(first, second)
# ans = 0
# class dot():
#     def __init__(self) -> None:
#         self.d = {(0, -1):False, (1,0):False, (0,1):False, (-1,0):False}
# dots = [[dot() for i in range(6)] for j in range(6)]
# grid = [["*" for _ in range(5)] for x in range(5)]

# def move(player, p, m):
#     p += m
#     if p >= 37:
#         p -= 36
#     dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]
#     if player == 1:
#         dir = [dir[0]] + dir[1:][::-1]
    
#     placed = False
#     while True:
#         x = (p-1)%6
#         y = (p-1)//6
#         for dx, dy in dir:
#             nx, ny = x+dx, y+dy
#             if 0 <= nx <= 5 and 0 <= ny <= 5:
#                 if not dots[y][x].d[(dx,dy)]:
#                     dots[y][x].d[(dx,dy)] = True
#                     dots[ny][nx].d[(-dx, -dy)] = True
#                     placed = True
#                     break
#         if placed:
#             break
#         p += 1
#         if p >= 37:
#             p = 1
#     return p

# def check(p):
#     c = 0
#     for y in range(5):
#         for x in range(5):
#             if grid[y][x] == "*":
#                 if dots[y][x].d[(1,0)] and dots[y][x].d[(0,1)] and dots[y+1][x+1].d[(-1,0)] and dots[y+1][x+1].d[(0,-1)]:
#                     grid[y][x] = p
#                     c += 1
#     return c
# for p1 in range(1, 37):
#     for m1 in range(1, 36):
#         for p2 in range(1, 37):
#             for m2 in range(1, 36):
#                 dots = [[dot() for i in range(6)] for j in range(6)]
#                 grid = [["*" for _ in range(5)] for x in range(5)]
#                 second = 0
#                 turn = 0
#                 for _ in range(60):
#                     if turn == 0: #player 1
#                         p1 = move(0, p1, m1)
#                         won = check("X")
#                         if won == 0:
#                             turn = 1
#                         else:
#                             break

#                     else: #player 2
#                         p2 = move(1, p2, m2)
#                         won = check("O")
#                         second += won
#                         if won == 0:
#                             turn = 0
#                 if second == 25:
#                     ans += 1
# print(ans)
