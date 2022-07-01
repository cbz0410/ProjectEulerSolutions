def get_cycle_length(n):
    remainders = [0 for i in range(n)]
    value = 1
    index = 0

    while remainders[value] == 0 and value != 0:
        remainders[value] = index
        value = value * 10 % n
        index += 1

    return index - remainders[value]

def compute_largest_cycle_length():
    largest_length = 0

    for i in range(1000, 1, -1):
        if largest_length > i:
            break

        current_length = get_cycle_length(i)
        if(current_length > largest_length):
            largest_length = current_length

    return largest_length

if __name__ == '__main__':
    print(compute_largest_cycle_length())