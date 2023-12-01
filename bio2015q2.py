a, c, m = [int(i) for i in input().split()]
r = 0
ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
grid = {(x,y):-1 for x in range(10) for y in range(10)}

def check(coords, i):
	for f, g in coords:
		x2, y2 = x+f+(i*u), y+g+(i*t)
		if y2 < 0 or y2 >= 10 or x2 < 0 or x2 >= 10:
			if [f,g] == [0,0]:
				return False
			continue
		if grid[(x2, y2)] != -1:
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
			mid = [[0, -1],[0, 1],[0,0]]
			end = [[1,1],[1,0],[1,-1]]
		else:
			orientation = 'V'
			t = 1
			u = 0
			start = [[-1,-1],[1,-1],[0,-1]]
			mid = [[-1,0],[1, 0],[0,0]]
			end = [[-1,1],[1,1],[0,1]]
		
		checks = [check(start, 0), check(end, length-1)]
		if all(checks):
			for i in range(length):
				valid = check(mid, i)
				if not valid:
					break
			if valid:
				for i in range(length):
					grid[(x+(i*u), y+(i*t))] += 1
				print(x, y, orientation)