class Test:
    def __init__(self):
        self.customer = 'mycustomer'

    @classmethod
    def main(cls, customer):
        customer = self.customer
        print('from main {}'.format())


if __name__ == '__main__':
    Test.main()
    # main()
    # if __name__ == '__main__':

