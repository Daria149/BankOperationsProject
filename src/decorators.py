from collections.abc import Callable
from functools import wraps
from time import time
from typing import Any


def log(file_name: Any = None) -> Callable:
    """Декоратор для логирования функции."""

    def decorator_func(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                time_1 = time()
                result = func(*args, **kwargs)
                time_2 = time()
                if file_name:
                    with open(file_name, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} OK\n")
                        file.write(f"Начало работы функции: {time_1}\n")
                        file.write(f"Документация функции {func.__name__}: {func.__doc__}\n")
                        file.write(f"Результат работы функции: {result}\n")
                        file.write(f"Конец работы функции: {time_2}\n")
                else:
                    print(f"{func.__name__} OK\n")
                    print(f"Начало работы функции: {time_1}\n")
                    print(f"Документация функции {func.__name__}: {func.__doc__}\n")
                    print(f"Результат работы функции: {result}\n")
                    print(f"Конец работы функции: {time_2}\n")
            except Exception as e:
                if file_name:
                    with open(file_name, "a", encoding="utf-8") as file:
                        file.write(f"Ошибка функции {func.__name__}: {e}. Input: {args}, {kwargs}")
                else:
                    print(f"Ошибка функции {func.__name__}: {e}. Input: {args}, {kwargs}")
            return result

        return wrapper

    return decorator_func


@log(file_name="")
def result_function(x: int, y: int) -> Any:
    """Функция, возводящая в степень."""
    result_of_function = x**y
    return result_of_function


print(result_function(1, 2))
