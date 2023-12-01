# from operator import mul
# from functools import reduce
# from math import sqrt
# n = int(input())

# primes = set()
# primes.add(2)
# prime = 2
# used = set()
# valid = True
# for i in range(5, int(sqrt(n))+1, 6):
#     if n % i == 0:
#         valid = False
#         break
# if valid:
#     print(n)
# else:
#     def is_prime(n):
#         if n == 2 or n == 3:
#             return True
#         elif n <= 1 or n % 2 == 0 or n % 3 == 0:
#             return False
#         for p in primes:
#             if n % p == 0:
#                 return False
#         return True

#     while n != 1:
#         while n % prime == 0:
#             n //= prime
#             used.add(prime)
#         if prime == 2:
#             prime = 3
#         else:
#             prime += 2
#             while not is_prime(prime):
#                 prime += 2
#             primes.add(prime)
#     print(reduce(mul, used))

from operator import mul
from functools import reduce
primes = []
n = 1_000_000
d = {i:0 for i in range(n)}
#sieve of eratosthenes to generate primes up to n
sieve = [0 for i in range(n+1)]

for i in range(2, n+1):
    if sieve[i]:
        continue
    for j in range(2*i, n+1, i):
        sieve[j] = i

for i in range(2, n):
    if sieve[i] == 0:
        primes.append(i)

# for j in range(3, 1000000):
#     valid = True
#     if j % 2 == 0 or j % 3 == 0:
#         valid = False
#     else:
#         for i in primes:
#             if j % i == 0:
#                 valid = False
#                 break
#     if valid:
#         primes.append(j)
for n in range(2, 1_000_000):
    used = set()
    
    while n != 1:
        for prime in primes:
            if n % prime == 0:
                used.add(prime)
            while n % prime == 0:
                n //= prime
            if n == 1:
                break
                
    ans = reduce(mul, used)
    d[ans] += 1
print(max(d, key=lambda x:x.value()))