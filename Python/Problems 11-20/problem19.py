MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
 
def compute():
    day = 2
    sunday_count = 0
    for y in range(1901, 2001):
        for m in range(0, 12):
            day += MONTHS[m]

            if(y % 100 == 0):
                if(y % 400 == 0 and m == 1):
                    day += 1
            elif(y % 4 == 0 and m == 1):
                day += 1

            day %= 7

            if(day == 0):
                sunday_count += 1
    return sunday_count

if __name__ == '__main__':
    print(compute())