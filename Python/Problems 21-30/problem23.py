import math

a_nums = []
can_be_expressed = [False for i in range(28124)]

def a(n):
    sum = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum += i + n / i
        if i * i == n:
            sum -= i

    return int(sum) > n

def set_a_nums():
    for i in range(2, 28124):
        if(a(i)):
            a_nums.append(i)

def set_can_be_expressed():
    for i in range(len(a_nums)):
        for j in range(i, len(a_nums)):
            if(a_nums[i] + a_nums[j] <= 28123):
                can_be_expressed[a_nums[i] + a_nums[j]] = True

def sum_outliers():
    sum = 0
    for i in range(1, 28124):
        if not can_be_expressed[i]:
            sum += i

    return sum

if __name__ == '__main__':
    set_a_nums()
    set_can_be_expressed()
    print(sum_outliers())