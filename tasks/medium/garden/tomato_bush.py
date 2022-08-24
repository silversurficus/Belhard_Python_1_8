class TomatoBush:
    tomato_list: list

    def __init__(self, *args):
        self.tomato_list = []
        for argument in args:
            self.tomato_list.append(argument)

    def grow_all(self):
        for tomato in self.tomato_list:
            tomato.grow()

    def all_are_ripe(self):
        if all(tomato.is_ripe() for tomato in self.tomato_list):
            return True
        else:
            return False

    def give_away_all(self):
        indexes = []
        for tomato in self.tomato_list:
            indexes.append(tomato.index)
        self.tomato_list = []
        return indexes
