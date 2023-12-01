from functools import reduce
from operator import mul
from math import sqrt

n = int(input())

def is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(sqrt(n))+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

primes = set()
primes.add(2)
if is_prime(n):
    primes.add(n)

for num in range(3, n//2):
    prime = True
    for j in primes:
        if j > num:
            break
        if num % j == 0:
            prime = False
            break
    if prime:
        primes.add(num)

factors = set()
for i in primes:
    if n % i == 0:
        factors.add(i)
print(reduce(mul, factors))
