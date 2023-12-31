from collections import Counter
from math import factorial
arr = [int(i) for i in input().split()]
n = arr.pop(-1)
letters = 'ABCD'
available = []
for i in range(len(arr)):
    for _ in range(arr[i]):
        available.append(letters[i])
ans = ''
def perms(s, m):
    res = factorial(m)
    use = Counter(available)-Counter(s)
    for k in use:
        res //= factorial(use[k])
    return res

while available:
    done = set()
    for l in available:
        if l in done: # dont check perms beginning with a letter more than once
            continue
        done.add(l)
        if (x := perms(l, len(available)-1)) < n:
            # dont take
            n -= x
        else:
            # take current letter
            break
    ans += l
    available.remove(l)
print(ans)