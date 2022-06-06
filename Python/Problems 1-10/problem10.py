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

if __name__ == "__main__":
    limit = 2000000
    primes = e_sieve(limit)

    sum = 0
    for i in range(2, limit + 1):
        if (primes[i] == True):
            sum += i

    print(sum)