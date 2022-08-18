class House:
    adress: str
    area: int
    cost: int
    def __init__(self, adress, area, cost):
        self.area = area
        self.cost = cost
        self.adress = adress

    def increase_cost(self, incr):
        self.cost += incr

    def decrease_cost(self, incr):
        self.cost -= incr