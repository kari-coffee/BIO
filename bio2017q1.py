from time import time

s = input()

start = time()

rows = [s]
colours = ['R','G','B']

while len(s) > 1:
    new = ''
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            new += s[i]
        else:
            for colour in colours:
                if colour not in [s[i], s[i+1]]:
                    new += colour
    s = new
print(new)

print(time()-start)