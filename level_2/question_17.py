if __name__ == '__main__':
    total_amount = 0
    while True:
        values = input().split()
        if not values:
            break

        if values[0].lower() == 'd':
            total_amount += int(values[1])
        elif values[0].lower() == 'w':
            total_amount -= int(values[1])
        else:
            print('Invalid transaction', "\'" + ' '.join(values) + "\'")

    print('Total amount:', total_amount)
