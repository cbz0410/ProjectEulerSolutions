def find_solutions():
    solutions = []

    for i in range(2, 500000):
        if(calculate_digit_power_sum(i, 5) == i):
            solutions.append(i)

    return solutions

def calculate_digit_power_sum(n, power):
    sum = 0

    for s in str(n):
         value = int(s)
         sum += pow(value, power)

    return sum

if __name__ == '__main__':
    print(sum(find_solutions()))