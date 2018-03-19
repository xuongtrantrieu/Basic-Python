if __name__ == '__main__':
    table = []
    while True:
        values = tuple(input().split())
        if not values:
            break
        table.append(values)
    print(sorted(sorted(sorted(table, key=lambda x: x[2]), key=lambda x: x[1]), key=lambda x:x[0]))