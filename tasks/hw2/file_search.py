import os
import sys


def find_and_read_file(filename):
    current_dir = os.getcwd()
    
    for root, _, files in os.walk(current_dir):
        if filename in files:
            file_path = os.path.join(root, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = [next(f) for _ in range(5)]
                    print(f'\nФайл найден в директории: {root}')
                    print('\nПервые 5 строк файла:')
                    print(''.join(lines))
                return True
            except Exception as e:
                print(f'\nФайл найден в директории: {root}')
                print(f'Ошибка при чтении файла: {str(e)}', file=sys.stderr)
                return False
    return False


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Использование: python file_search.py <имя_файла>', file=sys.stderr)
        sys.exit(1)
    
    filename = sys.argv[1]
    if not find_and_read_file(filename):
        print(f'Файл {filename} не найден', file=sys.stderr)
        sys.exit(1)
