class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Садовник работает...')
        self._plant.grow_all()
        print('Садовник закончил работу')

    def harvest(self):
        print('Сборка урожая...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Сборка урожая окончена')
        else:
            print('Урожай не созрел!')

    @staticmethod
    def knowledge_base():
        print('''Сборку урожая проводят, когда помидор красный.''')