import datetime
from functools import wraps
from typing import Any, Callable


def function_logger(log_file: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = datetime.datetime.now()
            
            args_str = str(args) if args else '()'
            kwargs_str = str(kwargs) if kwargs else '{}'
            args_line = f"{args_str}, {kwargs_str}" if args and kwargs else args_str or kwargs_str
            
            result = func(*args, **kwargs)
            
            end_time = datetime.datetime.now()
            execution_time = end_time - start_time
            
            result_str = str(result) if result is not None else '-'
            time_str = str(execution_time).split('.')[0]
            
            with open(log_file, 'a', encoding='utf-8') as f:
                f.write(f"{func.__name__}\n")
                f.write(f"{start_time.strftime('%Y-%m-%d %H:%M:%S.%f')}\n")
                f.write(f"{args_line}\n")
                f.write(f"{result_str}\n")
                f.write(f"{end_time.strftime('%Y-%m-%d %H:%M:%S.%f')}\n")
                f.write(f"{time_str}\n")
            
            return result
        return wrapper
    return decorator


@function_logger('tasks/lab2/files/test.log')
def greeting_format(name):

    return f'Hello, {name}!'


if __name__ == '__main__':
    greeting_format('John')
