import itertools

permutations = [''.join(i) for i in itertools.permutations('0123456789')]
permutations = sorted(permutations)

if __name__ == '__main__':
    print(permutations[999999])