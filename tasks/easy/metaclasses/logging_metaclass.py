"""
Написать логгирующий декоратор log_decorator, который будет логгировать
вызов функции. До выполнения функции необходимо вывести в консоль строку
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}". А после вывести
строку "Выполнено {func.__name__}".

Написать логгирующий метакласс LogMeta, который ко всем методам класса добавляет
функционал декоратора log_decorator.
"""
import time

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Выполняем {func.name} с args: {args} и kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Выполнено {func.name}")
        return result
    return wrapper


class LogMeta(type):

    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if ((not name.startswith('')) and callable(value)))
        decorated_attr = dict((name, log_decorator(value)) for name, value in attrs)
        return super(LogMeta, cls).__new__(cls, name, bases, decorated_attr)

class Hahaha(metaclass = LogMeta):
    def fff(self, x):
        time.sleep(3)
        return "fff"

    def hhh(self):
        time.sleep(3)
        return "hhh"

h = Hahaha()
h.fff(1)
h.hhh()