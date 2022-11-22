s = input()
total = 0

for i in range(len(s)):
    if s[i] == '?':
        missing = 10-i
    elif s[i] == 'X':
        total += 10*(10-i)
    else:
        total += int(s[i])*(10-i)
if total % 11 == 0:
    print(0)
else:
    c = 0
    while total % 11 != 0:
        total += missing
        c += 1
    print('X') if c == 10 else print(c)