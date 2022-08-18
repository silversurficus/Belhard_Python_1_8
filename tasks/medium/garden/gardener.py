class Gardener:
    name: str
    plants: list
    def __init__(self, name, *args):
        self.name = name
        self.plants = []
        for argument in args:
            self.plants.append(argument)

    def work(self):
        for tomato_bush in self.plants:
            tomato_bush.grow_all()

    def harvest(self):
        if all(tomato_bush.all_are_ripe() for tomato_bush in self.plants):
            tomato_list = []
            for tomato_bush in self.plants:
                tomato_list += tomato_bush.give_away_all()
            return tomato_list
        else:
            print("Томаты еще не созрели")
            return None