def count_upper(text):
    result = 0
    for x in text:
        if x.isupper():
            result += 1
    return result

def count_lower(text):
    result = 0
    for x in text:
        if x.islower():
            result += 1
    return result

if __name__ == '__main__':
    text = input()
    print('UPPER CASE', count_upper(text))
    print('LOWER CASE', count_lower(text))
