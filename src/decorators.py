from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования выполнения функции. Если filename задан, данные
    записываются в файл "mylog.txt", иначе выводятся в консоль."""

    def decorator(func: Callable) -> Callable:
        """Возвращает обёртку, которая логирует выполнение функции 'func'"""

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Обёртка для выполнения функции 'func' с логированием ее результата
            и ошибок."""
            try:
                result = func(*args, **kwargs)
                name_func = func.__name__
                if filename:
                    file = open(filename, "a", encoding="utf-8")
                    file.write(f"Функция {name_func} ок. Результат: {result}" + "\n")
                    file.close()
                else:
                    print(f"{name_func} ок. Результат: {func(*args, **kwargs)}")
            except Exception as e:
                result = None
                print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
            return result

        return wrapper

    return decorator
