import math

def is_prime(n):
    if (n == 2):
        return True

    for i in range(2, (int)(math.sqrt(n)) + 2):
        if (n % i == 0):
            return False

    return True

if __name__ == "__main__":
    count = 1
    answer = 1

    while (count < 10001):
        answer += 2

        if (is_prime(answer)):
            count += 1

    print(answer)