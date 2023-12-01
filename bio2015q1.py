# a) [23]
# (did part b & c on paper, [2], [2/6])
s = input()

def find(s):
    ans = 0
    for i in range(1, len(s)//2+1):
        block = ''
        for j in range(i):
            block += s[j]
        if s[-(i):] == block:
            ans += 1 + find(s[i:-(i)])
    return ans

print(find(s))