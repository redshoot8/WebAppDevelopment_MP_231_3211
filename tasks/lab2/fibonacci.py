cube = lambda x: x ** 3


def fibonacci(n):
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    return fibonacci(n - 1) + [fibonacci(n - 1)[-1] + fibonacci(n - 1)[-2]]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
