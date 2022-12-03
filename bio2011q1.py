a, b, n = input().split()
n = int(n)
a = ord(a)-64
b = ord(b)-64
arr = [b]
for i in range(n-2):
    temp = a
    a = b
    b += temp
    if b > 26:
        b -= 26
    arr.append(b)
print(chr(b+64))
print(arr)
