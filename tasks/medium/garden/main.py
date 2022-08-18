from tomato import Tomato
from tomato_bush import TomatoBush
from gardener import Gardener


if __name__ == '__main__':
    tomatobush1 = TomatoBush(Tomato(1), Tomato(2), Tomato(3), Tomato(4), Tomato(5))
    tomatobush2 = TomatoBush(Tomato(6), Tomato(7), Tomato(8), Tomato(9))
    gardener = Gardener("aaa", tomatobush1, tomatobush2)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    print(gardener.harvest())
    gardener.work()
    gardener.harvest()