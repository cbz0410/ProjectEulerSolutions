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

def find_fib_term_with_digits(max):
    i = 1
    while len(str(fib(i))) < max:
        i += 1

    return i
    
if __name__ == '__main__':
    print(find_fib_term_with_digits(1000))