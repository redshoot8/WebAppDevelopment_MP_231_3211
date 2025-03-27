def my_sum(*args):
    return sum(args)


if __name__ == '__main__':
    print(my_sum(*map(int, input().split())))
