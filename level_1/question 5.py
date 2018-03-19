class Basic:
    def __init__(self, text=''):
        self.text = text
        return

    def getString(self, text):
        self.text = text

    def printString(self):
        print(self.text)

    def __str__(self):
        return self.text

if __name__ == '__main__':
    a = Basic('a')
    a.getString('abc')
    a.printString()
    # print(a)
