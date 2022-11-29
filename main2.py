import os
from datetime import datetime

def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            date = datetime.now()
            name = old_function.__name__
            with open(path, 'a', encoding='utf-8') as f:
                f.write(
                    f'Дата и время обращения {date}\n'
                    f'Имя функции {name}\n'
                    f'Аргументы функции {args} {kwargs}\n'
                    f'\n'
                )
        return new_function

    return __logger


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        hello_world()

        @logger(path)
        def summator(a, b=0):
            return a + b

        summator(4, 0)

        @logger(path)
        def div(a, b):
            return a / b

        div(5, 6)

if __name__ == '__main__':
    test_2()