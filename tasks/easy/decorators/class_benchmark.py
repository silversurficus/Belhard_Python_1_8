"""
Написать декоратор класса class_benchmark, который будет проводить
бенчмарк (замер времени выполнения) всех публичных методов класса
(те, которые не начинаются с _).

Чтобы у методов класса изменить поведение - дополнительно написать
декоратор функции def_benchmark.

До выполнения метода должен быть вывод в консоль:
Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}
Время начала: {start_time}

После выполнения метода должен быть вывод в консоль:
Выполнено {func.__name__}
Время окончания: {end_time}
Всего затрачено времени на выполнение: {end_time - start_time}
"""
import time




def func_benchmark(func):
    def wrapper(*args, **kwargs):
        print(f"Выполняем {func.__name__} с args: {args[0:]} и kwargs: {kwargs}")
        start_time = time.time()
        print(f"Время начала: {start_time}")
        result = func(*args, **kwargs)
        print(f"Выполнено {func.__name__}")
        end_time = time.time()
        print(f"Время окончания: {end_time}")
        print(f"Всего затрачено времени на выполнение: {end_time - start_time}")
        return result
    return wrapper

def class_benchmark(cls):
    call_attr = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for name, val in call_attr.items():
        decorated = func_benchmark(val)
        setattr(cls, name, decorated)
    return cls

@class_benchmark
class SomeClass:
    def __init__(self):
        pass
    def say_hi(self):
        print("Hi")
        print("Hi")
        print("Hi")
        print("Hi")
        print("Hi")
        print("Hi")
        time.sleep(4)
        print("Hi")
        print("Hi")

obj = SomeClass()
obj.say_hi()