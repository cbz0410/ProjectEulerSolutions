def square_of_sum(n):
    sum = 0

    for i in range(n + 1):
        sum += i

    return sum * sum

def sum_of_square(n):
    sum = 0

    for i in range(n + 1):
        sum += i * i

    return sum

if __name__ == '__main__':
    print(square_of_sum(100) - sum_of_square(100))