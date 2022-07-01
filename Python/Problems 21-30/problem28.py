def sum_left_diagonal(bound):
    sum = 1

    for n in range(2, bound + 1):
        product = n * n + 1 if n % 2 == 0 else n * n
        sum += product

    return sum

def sum_right_diagonal(bound):
    sum = 0
    previous_term = 1

    for n in range(1, bound):
        current_term = previous_term + 2 * n
        sum += current_term

        previous_term = current_term

    return sum

def sum_diagonals(bound):
    return sum_right_diagonal(bound) + sum_left_diagonal(bound)

if __name__ == '__main__':
    print(sum_diagonals(1001))