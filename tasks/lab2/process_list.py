import timeit


# Версия с List Comprehension: 0.00000054 сек за вызов
def process_list(arr):
    result = [i ** 2 if i % 2 == 0 else i ** 3 for i in arr]
    return result


# Версия-генератор: 0.00000015 сек за вызов
def process_list_gen(arr):
    return (i ** 2 if i % 2 == 0 else i ** 3 for i in arr)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    iterations = 10000

    rec_time = timeit.timeit(lambda: process_list(arr), number=iterations)
    it_time = timeit.timeit(lambda: process_list_gen(arr), number=iterations)

    print(f'Версия с List Comprehension: {rec_time/iterations:.8f} сек за вызов')
    print(f'Версия-генератор: {it_time/iterations:.8f} сек за вызов')
