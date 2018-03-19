def double_number_dict(n):
    d = dict()
    for x in range(n + 1):
        d[x] = x * x

    return d

if __name__ == '__main__':
    size = int(input('Input dict length: '))
    print(double_number_dict(size))

