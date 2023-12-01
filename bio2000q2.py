grid = [['.' for i in range(11)] for j in range(11)]
x1, y1, d1 = input().split()
x2, y2, d2 = input().split()

x1 = int(x1)-1
y1 = int(y1)-1
x2 = int(x2)-1
y2 = int(y2)-1
conversions = {'T':0, 'R':1, 'B':2, 'L':3}
reverse_conversions = {v:k for k, v in conversions.items()}
d1 = conversions[d1]
d2 = conversions[d2]
dirs = {3:(-1, 0), 1:(1, 0), 0:(0, 1), 2:(0, -1)}

def move(d, x, y):
    x += dirs[d][0]
    y += dirs[d][1]
    if 0 <= y < 11 and 0 <= x < 11:
        if grid[y][x] == '.':
            grid[y][x] = '*'
            d = (d+1)%4
        else:
            grid[y][x] = '.'
            d = (d-1)%4
        return d, x, y
    else:
        return -1, -1, -1

n = input()
while n != '-1':
    if n.isdigit():
        n = int(n)
        for i in range(n):
            if d1 != -1:
                d1, x1, y1 = move(d1, x1, y1)
            if d2 != -1:
                d2, x2, y2 = move(d2, x2, y2)

        for row in range(10, -1, -1):
            print(''.join(grid[row]))
        if d1 != -1:
            print(x1+1, y1+1, reverse_conversions[d1])
        else:
            print('Removed')
        if d2 != -1:
            print(x2+1, y2+1, reverse_conversions[d2])
        else:
            print('Removed')
    n = input()