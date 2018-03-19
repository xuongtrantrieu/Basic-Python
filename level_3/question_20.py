class Divisible_by_7():
    def __init__(self, min=0, max=7):
        self.min = min
        self.max = max
        self.first_divisible()

    def first_divisible(self):
        x = self.min
        while True:
            if x % 7 == 0:
                self.first_seven = x
                break
            else:
                x += 1

    def get_it(self):
        x = self.first_seven
        while x <= self.max:
            yield x
            x += 7


if __name__ == '__main__':
    a = Divisible_by_7(0, 1000)
    for x in a.get_it():
        print(x)

