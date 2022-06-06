memo = {}
def memoize_fib(func):
    
    def inner(n):
        if n not in memo:
            ans = func(n)
            memo[n] = ans
            return ans
        else:
            return memo[n]

    return inner

@memoize_fib
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    i, sum = 0, 0
    value = fib(i)

    while value <= 4000000:
        if value % 2 == 0:
            sum += value
        
        i = i + 1
        value = fib(i)

    print(sum)