import os
from datetime import datetime

def logger(old_function):
    def new_function(*args, **kwargs):
        date = datetime.now()
        name = old_function.__name__
        result = old_function(*args, **kwargs)
        with open('main.log', 'a',  encoding='utf-8') as f:
            f.write(
                f'Дата и время обращения {date}\n'
                f'Имя функции {name}\n'
                f'Аргументы функции {args} {kwargs}\n'
                f'\n'
            )
        return result

    return new_function


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    hello_world()

    @logger
    def summator(a, b=0):
        return a + b

    summator(4, 0)

    @logger
    def div(a, b):
        return a / b

    div(5, 6)

if __name__ == '__main__':
    test_1()
