# a) [24]
# b) 832040 [2]
# c) 16215 (47C3) x 18424 (49C3)
# d) x 

n = int(input())
fib = [1, 2]
i = 1
while fib[i] <= n:
    i += 1
    fib.append(fib[i-1]+fib[i-2])
used = []
for i in range(len(fib)-1, -1, -1):
    if fib[i] <= n:
        n -= fib[i]
        used.append(fib[i])
    if n == 0:
        break
print(*used)

