# a) [24]
# b) LKBXIY [3]
# c) No, as only half of the letters are ever used, since the shift is always
# by 1, each time you move to the next character, it always skips one letter
# So when you get to halfway (letter N), it will loop back to the start, for example
# ABCDEFGHIJKLM ABCDEFGHIJKLM [4]
# d) Some maths with cycles - find cycle with subcycles that add to 26, and that are
# coprime to get the maximum cycle length (1260)
n, s = input().split()
n = int(n)-1
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# generate decoder ring
ring = []
pos = 0
letters = list(alpha)
while letters:
    pos = (pos+n)%len(letters)
    ring.append(letters.pop(pos))
print(''.join(ring[:6]))

# encrypt s
def encrypt(l, shift):
    return ring[(alpha.index(l)+shift)%len(ring)]

ans = ''
shift = 0
for l in s:
    ans += encrypt(l, shift)
    shift += 1
print(ans)
