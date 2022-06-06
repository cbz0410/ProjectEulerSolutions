def is_palindrome(n):
    if (str(n) == str(n)[ : : -1]):
        return True
    
    return False

if __name__ == '__main__':
    answer = 0

    for x in range(100, 1000):
        for y in range(100, 1000):
            if(is_palindrome(x * y) and x * y > answer):
                answer = x * y

    print(answer)