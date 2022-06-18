import math

def num_divisors(n):
    count = 0
    sqrt = (int)(math.sqrt(n))

    for i in range(1, sqrt + 1):
        if (n % i == 0):
            count += 2
        
    if (sqrt * sqrt == n):
        count -= 1

    return count

if __name__ == '__main__':
    contFlag = True

    sum = 0
    natNum = 1
    while(contFlag):
        sum += natNum

        if(num_divisors(sum) > 500):
            contFlag = False

        natNum += 1

    print(sum)