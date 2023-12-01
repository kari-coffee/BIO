s = input()
if len(s) == 1:
    valid = True
else:
    for i in range(1, len(s)//2+1):
        last = s[:i]
        valid = True
        for j in range(i, len(s)-i+1, i):
            if last == s[j:j+i]:
                valid = False
                break
            last = s[j:j+i]

        if not valid:
            break
if valid:
    print('Accepted')
else:
    print('Rejected')