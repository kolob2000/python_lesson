from functools import wraps


def type_log(func):
    @wraps(func)
    def log_wrapper(*args, **kwargs):
        print(f'{type(func(*args, **kwargs))} {func.__name__}(', end='')
        for i in args:
            print(f'{i}: {type(i)}, ', end='')
        for j, k in kwargs.items():
            print(f'{j}={k}: {type(k)},', end='')
        print(')')
        return func(*args, **kwargs)

    return log_wrapper


@type_log
def add(a=1, b=7):
    return a + b


print(add(7.0, b=24))
print(add.__name__, 'декоратор замаскирован)')
