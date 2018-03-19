from collections import Counter

if __name__ == '__main__':
    words = sorted(input('Input: ').split())
    print(words)
    for key, value in sorted(Counter(words).items(), key=lambda x: x[0]):
        print(key + ':' + str(value))