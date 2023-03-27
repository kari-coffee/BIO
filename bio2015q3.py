from math import factorial
from collections import Counter

a, b, c, d, n = [int(i) for i in input().split()]
x = [a, b, c, d]
chars =  ['A', 'B', 'C', 'D']
letters = []
for i in range(4):
    for _ in range(x[i]):
        letters.append(chars[i])
res = ''

def perms(s):
    res = factorial(len(s))
    for l, rpt in Counter(s).items():
        res //= factorial(rpt)
    return res

while letters:
    choice = 0
    considered = set()
    while True:
        if letters[choice] not in considered:
            remaining = list(letters)
            remaining.remove(letters[choice])
            if (step_over := perms(remaining)) >= n:
                break
            considered.add(letters[choice])
            n -= step_over
        choice += 1

    res += letters.pop(choice)

print(res)
