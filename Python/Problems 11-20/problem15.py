# the solution is just 2n choose n, where n is the length of the square grid
def factorial(n):
    product = 1

    for i in range(1, n + 1):
        product *= i
    
    return product

def two_n_choose_n(x, y):
    return (int)(factorial(x) / factorial(y) ** 2)

if __name__ == '__main__':
    print(two_n_choose_n(40, 20))