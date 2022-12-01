a, c, m = [int(i) for i in input().split()]
r = 0
ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
#grid = [[-1 for i in range(10)] for j in range(10)]
grid = {(y,x):-1 for y in range(10) for x in range(10)}

def check(coords, i):
	for f, g in coords:
		y2, x2 = y+g+(i*t), x+f+(i*u)
		if y2 < 0 or y2 >= 10 or x2 < 0 or x2 >= 10: 
			continue
		if grid[(y2, x2)] != -1:
			return False
	return True

for length in ships:
	valid = False
	while not valid:
		r = (a*r+c) % m
		r = str(r)
		x = int(r[-1])
		if len(r) == 1:
			y = 0
		else:
			y = int(r[-2])
		r = int(r)
		r = (a*r+c) % m
		
		if r % 2 == 0:
			orientation = 'H'
			t = 0
			u = 1
			start = [[-1,1],[-1,-1],[-1,0]] # [x,y]
			mid = [[0,-1],[0,1],[0,0]]
			end = [[1,1],[1,0],[1,-1]]
		else:
			orientation = 'V'
			t = -1
			u = 0
			start = [[-1,1],[1,1],[0,1]]
			mid = [[-1,0],[1,0],[0,0]]
			end = [[-1,-1],[1,-1],[0,-1]]
		
		checks = [check(start, 0), check(end, length-1)]
		if all(checks):
			for i in range(length):
				valid = check(mid, i)
				if not valid:
					break
			if valid:
				for i in range(length):
					grid[(y+(i*t), x+(i*u))] = 1
				print(x, y, orientation)