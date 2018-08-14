import numpy as np

def isPrime(n):
    if len([n % x for x in range(1, n+1) if n % x == 0]) == 2:
        return True
    else:
        return False


def OccurencesOfPrimes(ls: list):
    return sum([1 for x in ls if isPrime(x)])


def SumIf(a,b):
    return sum(np.setxor1d(a,b))
