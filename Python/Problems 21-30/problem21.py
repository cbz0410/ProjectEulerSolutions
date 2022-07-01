import math

memo = {}
def memoize_d(func):
    def inner(n):
        if n not in memo:
            ans = func(n)
            memo[n] = ans
            return ans
        else:
            return memo[n]

    return inner

@memoize_d
def d(n):
    sum = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum += i + n / i
        if i * i == n:
            sum -= i

    return int(sum)

def sum_amicable_pairs(max):
    sum = 0;
    for i in range(2, max):
        c_result = d(i)
        if(i == d(c_result) and c_result != i):
            sum += i

    return sum


if __name__ == '__main__':
    print(sum_amicable_pairs(10000))