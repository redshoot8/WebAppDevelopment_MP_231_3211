def sum_and_sub(a: float, b: float):
    return a + b, a - b


if __name__ == '__main__':
    print(*sum_and_sub(int(input()), int(input())))
