if __name__ == '__main__':
    result = []
    for x in range(1000, 3001):
        if x % 2 == 0:
            result.append(x)

    print(*result)
