from house import House
from townhouse import Townhouse
from person import Person

if __name__ == '__main__':
    house1 = House("aaa", 120, 50000)
    house2 = House("bbb", 40, 15000)
    house3 = House("ccc", 230, 160000)
    townhouse1 = Townhouse("ddd", 33000)
    townhouse2 = Townhouse("eee", 47000)
    townhouse3 = Townhouse("fff", 133000)
    person = Person("name", 33)
    person.earn_money(149000)
    person.info()
    person.make_deal(townhouse3)
    person.info()
    person.make_deal(house2)
    person.info()
    person.make_deal(house3)
    person.make_deal(townhouse2)
    person.info()
    pass
