# a) [23]
# b) 15 [2]
# c) Largest size 6, no idea [2/4]
# d) Yes, as each digit can always be reached by another digit even 
# if it needs to use other digit(s) to bridge the gap [3/6]

from collections import Counter
from collections import deque
from time import time
digits = {1:'ONE', 2:'TWO', 3:'THREE', 4:'FOUR', 5:'FIVE', 6:'SIX', 7:'SEVEN', 8:'EIGHT', 9:'NINE', 0:'ZERO'}
letters = [Counter(digits[i]) for i in range(10)]
valid = []
for a in letters:
    if a not in valid:
        valid.append(a)
    for b in letters:
        y = a+b
        if y not in valid:
            valid.append(y)
        for c in letters:
            x = a+b+c
            if x not in valid:
                valid.append(x)

for _ in range(3):
    s, f = input().split()
    start = time()
    cur = Counter(''.join([digits[int(i)] for i in s]))
    target = Counter(''.join([digits[int(i)] for i in f]))
    queue = deque([(cur, 0)])
    use = []
    x = sum((cur-target).values())+sum((target-cur).values())
    for v in valid:
        if sum((v-target).values())+sum((target-v).values()) < x:
            use.append(v)
    best = 100
    while queue:
        cur, steps = queue.popleft()
        x = sum((cur-target).values())+sum((target-cur).values())
        if x > best:
            continue
        else:
            best = x
        if cur == target:
            break
        for v in use:
            if sum((v-cur).values())+sum((cur-v).values()) <= 5 and sum((v-target).values())+sum((target-v).values()) < x:
                queue.append((v, steps+1))
    print(steps)
    print(time()-start)
