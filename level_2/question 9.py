if __name__ == '__main__':
    lines = ''
    while True:
        line = input()
        if line == '':
            break
        else:
            lines += line + '\n'
    print(lines.upper())
