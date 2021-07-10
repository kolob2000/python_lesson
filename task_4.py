from functools import wraps


def val_checker(verbosity):
    def _val_checker(func):
        @wraps(func)  # Скрываем декоратор
        def wrapper(*args, **kwargs):
            if verbosity(args[1]):
                return func(*args, **kwargs)
            else:
                raise ValueError('division by zero')

        return wrapper

    return _val_checker


@val_checker(lambda b: b > 0)
def my_div(a, b=0):
    print(a / b)


my_div(5, 4)
