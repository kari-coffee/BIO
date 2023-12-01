# MARKS
# a) [25]
# b) [3]
# c) [0]

#b) 0, 8, 9, 16, 18
#c) 1439  (wrong - 1440, I put hours += 1 after break)
f, s = [int(i) for i in input().split()]

first = [0, 0] #hours, minutes
second = [0, 0]
def calc(clock, i):
    mins = clock[1] + i+60
    clock[0] += mins // 60
    mins %= 60
    clock[1] = mins
    clock[0] %= 24
    return clock
while True:
    first = calc(first, f)
    second = calc(second, s)
    if first == second:
        break
    #hours += 1

ans = ["", ""]
for i in range(2):
    t = first[i]
    if t < 10:
        ans[i] = '0'+str(t)
    else:
        ans[i] = str(t)

print(f"{ans[0]}:{ans[1]}")
    