from math import sqrt

n = int(input())
res = 1


def is_prime(n):
    # simplest and most efficient algorithm for finding primes I found
    if n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False
    elif n == 2 or n == 3:
        return True
    
    for i in range(5, int(sqrt(n))+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

if is_prime(n):
    print(n)

    # V1
# else:
#     #find all primes up to n (maybe don't need to check all the way up to n?)
#     primes = [2, 3]
#     for i in range(5, n, 2):
#         if is_prime(i):
#             primes.append(i)
#     #print(primes)
#     #check which primes are factors
#     for i in primes:
#         if n % i == 0:
#             res *= i
#             #print(i)
            
#     print(res)

    # V2 - checks next prime only when needed - much faster!
else:
    done = False
    prime = 2
    for i in range(3, n, 2):
        if n == 1:
            break
        while n % prime == 0:
            n //= prime
            if not done:
                res *= prime
            done = True
        if is_prime(i):
            prime = i
            done = False
            
    print(res)
