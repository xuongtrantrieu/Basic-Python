if __name__ == '__main__':
    words = input().replace(' ', '').split(',')
    print((',').join(sorted(words)))
