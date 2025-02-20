def show_employee(name: str, salary: float = 100000):
    return f'{name}: {salary} ₽'


if __name__ == '__main__':
    print(show_employee('Иванов Иван Иванович', 30000))
