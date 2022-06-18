memo = {}
def memoize_collatz(func):

    def inner(n):
        if (n not in memo):
            ans = func(n)
            memo[n] = ans
            return ans
        else:
            return memo[n]

    return inner

@memoize_collatz
def collatz_length(n):
    if (n == 1):
        return 1
    if (n % 2 == 0):
        m = n / 2
    else:
        m = 3 * n + 1
    
    return collatz_length(m) + 1

if __name__ == '__main__':
    currentChain = 0
    longestChain = 0
    chainHolder = -1

    for i in range(1, 1000000):
        currentChain = collatz_length(i)

        if (currentChain > longestChain):
            longestChain = currentChain
            chainHolder = i
        
    print(chainHolder)