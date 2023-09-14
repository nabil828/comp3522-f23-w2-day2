class A:
    print('a')

    static_car = 2
    def __init__(self):
        print('A')


class B(A):
    print('b')
    def __init__(self):
        print('B')

def main():
    b = B()

main()