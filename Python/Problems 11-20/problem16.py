def sum_digits(str):
    sum = 0

    for i in str:
        sum += int(i)

    return sum

if __name__ == '__main__':
    number = 2 ** 1000

    print(sum_digits(str(number)))