def find_number(a, z):
    result = []
    for x in range(a, z + 1):
        if x % 7 == 0:
            if x % 5 != 0:
                result.append(x)
    return result

if __name__ == '__main__':
    print(find_number(2000, 3200))
