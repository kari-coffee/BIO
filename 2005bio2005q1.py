from math import gcd
a = float(input())
b = 1
while a != int(a):
    a *= 10
    b *= 10

a = int(a)
div = gcd(a, b)
while div != 1:
   a //= div
   b //= div
   div = gcd(a, b)
print(a, '/', b) 
