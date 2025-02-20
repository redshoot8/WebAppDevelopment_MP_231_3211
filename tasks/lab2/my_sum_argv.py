import sys


def my_sum(*args):
    return sum(args)


if __name__ == '__main__':
    if len(sys.argv) > 1: 
        numbers = map(int, sys.argv[1:])
        result = my_sum(*numbers)
        print(result)
    else:
        number = [int(num) for num in input('Введите числа через пробел: ').split()]
        result = my_sum(*number)
        print(result)
