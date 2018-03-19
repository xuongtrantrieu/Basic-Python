def is_even(x):
    if x % 2 == 0:
        return True
    return False

if __name__ == '__main__':
    numbers = [int(x) for x in input('Input: ').split(',')]
    odd_numbers = []
    for x in numbers:
        if not is_even(x):
            odd_numbers.append(x)
    print('Output:', ','.join([str(x) for x in odd_numbers]))
