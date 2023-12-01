# a) [23]
# b) [2]
# c&d not a clue (even having read ms)

flip = input()
last, next = list(input())
n = int(input())
curved = {'A':['E','F'],'B':['G','H'],'C':['I','J'],'D':['K','L'],'E':['M','N'],'F':['N','O'],'G':['O','P'],'H':['P','Q'],'I':['Q','R'],'J':['R','S'],'K':['S','T'],'L':['T','M'],'U':['M','N'],'V':['O','P'],'W':['Q','R'],'X':['S','T']}
for i in range(ord('D'), ord('L')):
    curved[chr(ord('M')+i-ord('D'))] = [chr(i), chr(i+1)]
curved['M'] = ['L', 'E']
straight = {'A':'D','B':'C','C':'B','D':'A','E':'A','F':'A','G':'B','H':'B','I':'C','J':'C','K':'D','L':'D','M':'U','N':'U','O':'V','P':'V','Q':'W','R':'W','S':'X','T':'X','U':'V','V':'U','W':'X','X':'W'}

class point():
    def __init__(self, left, right, straight, d):
        self.left = left
        self.right = right
        self.straight = straight
        self.d = d #-1 = left, 1 = right
points = {}
for p in curved:
    points[p] = point(curved[p][0], curved[p][1], straight[p], -1)

for _ in range(n):
    p = points[next]
    
    if p.straight == last:
        temp = next
        if p.d == -1:
            next = p.left
        else:
            next = p.right
        if temp in flip:
            p.d = -p.d
        last = temp
    else:
        temp = next
        if next not in flip:
            if p.left == last:
                p.d = -1
            else:
                p.d = 1
        next = p.straight
        last = temp
    print(last+next)
print(last+next)