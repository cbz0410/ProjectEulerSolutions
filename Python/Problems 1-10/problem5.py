def is_divisible(n):
    for i in range(1, 21):
        if (answer % i != 0):
            return False
        
    return True

if __name__ == '__main__':
    answer = 20

    while (not is_divisible(answer)):
        answer += 20

    print(answer)