from house import House
from townhouse import Townhouse


class Person:
    name: str
    age: int
    money: int
    realty: list
    def __init__(self, name, age):
        self.age = age
        self.name = name
        self.money = 0
        self.realty = []

    def info(self):
        print(f"name: {self.name} \n age: {self.age} \n money: {self.money} \n realty: {self.realty}")

    def earn_money(self, money):
        self.money += money

    def make_deal(self, object):
        if object.cost < self.money:
            self.money -= object.cost
            self.realty.append(object.adress)
        else:
            print("Недостаточно денег")

