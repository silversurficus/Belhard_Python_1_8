

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

    def make_deal(self, obj):
        if obj.cost < self.money:
            self.money -= obj.cost
            self.realty.append(obj.adress)
        else:
            print("Недостаточно денег")
