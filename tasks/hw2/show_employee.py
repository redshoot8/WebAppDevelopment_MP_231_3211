def show_employee(name: str, salary: int = 100000):
    return f'{name}: {salary} Р'


if __name__ == '__main__':
    name = input()
    salary = int(input())
    print(show_employee(name, salary))
