def cat_2_strings(s2, s3):
    return s2 + s3

def longer_string(s1, s2):
    if len(s1) > len(s2):
        return s1
    elif len(s2) > len(s1):
        return s2
    else:
        return [s1, s2]

def tell_even(number):
    try:
        number = int(number)
        if number % 2 == 0:
            return 'It is an even number'
        return 'It is an odd number'
    except:
        return 'Invalid value'

def square_an_even_array(array):
    return list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, array)))

def filter_practice(array):
    return list(filter(lambda x: x % 2 == 0 and x >= 1 and x <= 20, array))

class American:
    def __init__(self, name='Anonymous'):
        self.name = name

    @staticmethod
    def print_nationality():
        print('American')

    def __str__(self):
        return self.name

    pass

class Newyorker(American):
    def __init__(self, name='Anonymous'):
        American.__init__(self, name)

    pass

class Circle:
    def __init__(self, radius=0):
        self.radius = radius
        self.area = radius ** 2 * 3.14

    def __str__(self):
        return 'Radius: {}\nArea: {}'.format(self.radius, self.area)

    pass

class Rectangle:
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width
        self.area = self.length * self.width

    def __str__(self):
        return 'Rectange: {}x{}\nArea: {}'.format(self.length, self.width, self.area)
    pass

class Shape:
    def __calculate_area__(self):
        self.area = 0
    pass

class Square(Shape):
    def __init__(self, length=0):
        self.length = length
        self.__calculate_area__()

    def __calculate_area__(self):
        self.area = self.length ** 2

    def __str__(self):
        return 'Square: {length}x{length}\nArea: {}'.format(self.area, length=self.length)
    pass

def raise_error(error='RuntimeError'):
    raise RuntimeError(error)

def divide(a, b):
    try:
        return int(a) // int(b)
    except ZeroDivisionError:
        return 'Devided by zero'
    except ValueError:
        return 'Invalid value provided'
    except:
        print('Unknown error')
    finally:
        print('Hope that no error occurs')

class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def throw_error(self):
        raise self

    pass

def get_information_from_email(email):
    import re
    pattern = r'(.+)@(.+)(\.\w)+'
    information = re.match(pattern, email)
    print('Username: {}\nCompany Name: {}'.format(information.group(1), information.group(2)))

def draw_digits_from_text(text):
    # words = text.split()
    # result = []
    # for word in words:
    #     if word.isdigit():
    #         result.append(word)
    # return result

    import re
    pattern = r'\d+'
    return re.findall(pattern, text)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def gen_even(n):
    even = 0
    while even <= n:
        yield even
        even += 2
    return

def gen_5_and_7_divisible(n):
    div = 0
    while div <= n:
        yield div
        div += 35
    return

def make_sure_even(l):
    try:
        for x in l:
            assert x % 2 == 0
    except AssertionError:
        print('At least one number is not even')
        return False
    except TypeError as e:
        print(e)
        return False
    return True

def calculator():
    while True:
        try:
            command = input()
            if not command:
                break
            print('=\n' + str(eval(command)))
        except TypeError:
            print('Please enter valid value(s)')
        except SyntaxError:
            print('Please enter valid command')
        except ZeroDivisionError:
            print('Cannot divide by zero')
        except NameError:
            print('WTF??')
    return

def make_all_sentences():
    subjects = ["I", "You"]
    verbs = ["Play", "Love"]
    objects = ["Hockey","Football"]

    for s in subjects:
        for v in verbs:
            for o in objects:
                print(s, v, o)

    return

def remove_duplicate(l):
    result = list()
    seen = set()
    for x in l:
        if x not in seen:
            result.append(x)
            seen.add(x)
    return result

class Person:
    def __init__(self):
        return

    def get_gender(self):
        return self.__class__.__name__
    pass

class Male(Person):
    def __init__(self):
        return
    pass

class Female(Person):
    def __init__(self):
        return
    pass

def count_char(text):
    from collections import Counter
    for char, count in Counter(list([x.lower() for x in list(text.replace(' ', ''))])).items():
        print('\'{char}\': {count}'.format(char=char, count=count))
    return

def turn_100():
    from datetime import date
    age = int(input('Enter your age: '))
    print('You will turn 100 in {}'.format(date.today().year - age + 100))
    return

def even_or_odd():
    number = int(input('Your number is '))
    if number % 2 == 0:
        print('This is an even number')
    else:
        print('This is an odd number')
    return

def less_than_5():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print('Our list is', a)
    print('Less than 5 list is', list(filter(lambda x: x <= 5, a)))