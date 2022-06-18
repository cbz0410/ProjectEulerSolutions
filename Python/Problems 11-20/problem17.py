ONES = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "eighteen", "eighteen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def count_letters(n):
    str = ""
    count = 0

    if (1 <= n < 20):
        str += ONES[n]
    elif (20 <= n < 100):
        str += TENS[n // 10] + ONES[n % 10]
    elif (100 <= n < 1000):
        str += ONES[n // 100] + "hundred"
        n %= 100

        if (n != 0):
            str += "and"
            
            if (1 <= n < 20):
                str += ONES[n]
            elif (20 <= n < 100):
                str += TENS[n // 10] + ONES[n % 10]
    elif (n == 1000):
        str += "onethousand"

    for i in str:
        count += 1
    
    return count

if __name__ == '__main__':
    sum = 0

    for i in range(1, 1001):
        sum += count_letters(i)

    print(sum)