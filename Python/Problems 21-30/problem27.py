def e_sieve(limit):
    primes = [True for i in range(limit + 1)]
    primes[0], primes[1] = False, False

    p = 2
    while (p * p <= limit):
 
        if (primes[p] == True):
 
            for i in range(p * p, limit + 1, p):
                primes[i] = False

        p += 1
 
    return primes

def is_prime(n):
    return PRIMES[n]

def compute_ans():
    nL, aL, bL = 0, 0, 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0

            while is_prime(abs(n * n + a * n + b)):
                n += 1

            if n > nL:
                nL = n
                aL = a
                bL = b
    
    return aL * bL

PRIMES = e_sieve(100000)    
    
if __name__ == '__main__':
    print(compute_ans())