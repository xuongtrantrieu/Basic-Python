if __name__ == '__main__':
    numbers = [int(x) for x in input().split(',')]
    for x in numbers:
        if x < 1000 or x > 9999:
            numbers.remove(x)
    print(','.join(str(x) for x in numbers if x % 5 == 0))
