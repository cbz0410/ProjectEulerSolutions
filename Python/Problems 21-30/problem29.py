def calculate(bound):
    nums = []

    for a in range(2, bound + 1):
        for b in range(2, bound + 1):
            c_num = pow(a, b)
            if c_num not in nums:
                nums.append(c_num)

    return sorted(nums)

if __name__ == '__main__':
    print(len(calculate(100)))