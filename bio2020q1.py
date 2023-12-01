# a) [25]
s, n = input().split()
n = int(n)
letters = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
descending = sorted(letters, reverse=True)
memo = {}
def numeral(n):
    if n in memo:
        return memo[n]
    res = ''
    while n:
        for i in descending:
            if i <= n:
                n -= i
                res += letters[i]
                break
    memo[n] = res
    return res

def look_and_say(s):
    res = ''
    c = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            res += numeral(c)+s[i-1]
            c = 0
        c += 1
    
    return res+numeral(c)+s[-1]

for _ in range(n):
    s = look_and_say(s)
print(s.count('I'), s.count('V'))

# valid = [numeral(i) for i in range(8000)]
# b) [2]
# II, III, IV, IX
# for i in range(1, 4000):
#     s = numeral(i)
#     if look_and_say(s) in valid:
#         print(s)

# c) [4]
# 3919
# done = set()
# for i in range(1, 4000):
#     done.add(look_and_say(numeral(i)))
# print(len(done))