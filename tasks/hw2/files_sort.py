import os
import sys


def list_files_by_extension(directory_path):
    try:
        files = []
        for entry in os.listdir(directory_path):
            path = os.path.join(directory_path, entry)
            if os.path.isfile(path):
                files.append(entry)
        
        extension_groups = {}
        for filename in files:
            ext = os.path.splitext(filename)[1].lower() or '.no_extension'
            if ext not in extension_groups:
                extension_groups[ext] = []
            extension_groups[ext].append(filename)
        
        for ext in sorted(extension_groups.keys()):
            for filename in sorted(extension_groups[ext]):
                print(filename)
                
    except FileNotFoundError:
        print(f'Ошибка: Директория "{directory_path}" не найдена', file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f'Ошибка: Нет разрешения на чтение директории "{directory_path}"', file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f'Произошла ошибка: {str(e)}', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Использование: python script.py <путь_к_директории>', file=sys.stderr)
        sys.exit(1)
    
    directory_path = sys.argv[1]
    list_files_by_extension(directory_path)
