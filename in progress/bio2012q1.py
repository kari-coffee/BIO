from math import sqrt

n = int(input())
res = 1


def is_prime(n):
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

else:
    primes = [2, 3]
    for i in range(5, n, 2):
        if is_prime(i):
            primes.append(i)
    #print(primes)
    for i in primes:
        if n % i == 0:
            res *= i
            #print(i)
            
    print(res)
