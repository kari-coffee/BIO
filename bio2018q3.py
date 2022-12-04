from collections import defaultdict
from copy import deepcopy

d = int(input())
n = [int(i) for i in input()]
dists = defaultdict(lambda: 2**31)

def check(k, i, j, n):
    if (n[i] < n[k] < n[j]) or (n[j] < n[k] < n[i]):
        return True
    return False

def search(n, distance, visited):
    for i in range(d-1):
        j = i+1
        new = n[:i] + [n[j]] + [n[i]] + n[j+1:]
        temp = tuple(new)
        if temp not in visited:
            if i > 0:
                if check(i-1, i, j, n):
                    visited.add(temp)
                    dists[temp] = min(dists[temp], distance+1)
                    search(n[:i] + [n[j]] + [n[i]] + n[j+1:], distance+1, deepcopy(visited))
                    continue
                poss = True
            if j < d-1:
                if check(j+1, i, j, n):
                    visited.add(temp)
                    dists[temp] = min(dists[temp], distance+1)
                    search(n[:i] + [n[j]] + [n[i]] + n[j+1:], distance+1, deepcopy(visited))
                    continue
                poss = True
            if not poss:
                visited.add(temp)
    return distance
v = set()
v.add(tuple(n))
search(n, 0, deepcopy(v))
if len(dists) == 0:
    print(0)
else:
    print(max(dists.values()))