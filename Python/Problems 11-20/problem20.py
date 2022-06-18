def factorial(n):
    product = 1

    for i in range(2, n + 1):
        product *= i

    return product

def digit_sum(str):
    sum = 0

    for s in str:
        sum += int(s)

    return sum

if __name__ == '__main__':
    print(digit_sum(str(factorial(100))))