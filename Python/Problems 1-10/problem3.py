import math

def is_prime(n):
    for i in range(2, (int)(math.sqrt(n))):
        if (n % i == 0):
            return False

    return True

if __name__ == "__main__":
    biggestNum = 0
    num = 600851475143

    for i in range(2, (int)(math.sqrt(num))):
        if (num % i == 0 and is_prime(i)):
            biggestNum = i

    print(biggestNum)