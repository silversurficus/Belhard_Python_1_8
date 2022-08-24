"""
Напишите класс GameObject, в котором будут храниться координаты объекта.

- private атрибут x (тип int)
- private атрибут y (тип int)
- магический метод __init__, который принимает начальные x и y

Координаты должны быть доступны для чтения (сделать property), а их изменение
должно происходить в методе move(delta_x, delta_y). (изменение - это +=)
"""


class GameObject:

    _GameObject__x: int
    _GameObject__y: int

    def __init__(self, x, y):
        self._GameObject__x = x
        self._GameObject__y = y

    @property
    def x(self):
        return self._GameObject__x

    @property
    def y(self):
        return self._GameObject__y

    def move(self, delta_x, delta_y):
        self._GameObject__x += delta_x
        self._GameObject__y += delta_y
