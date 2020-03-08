class Player:

    def __init__(self, name):
        self._name = name
        self._age = None
        self._goals  = 0




    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def goals(self):
        return self._goals


    def score(self):
        self._goals += 1
        return self._goals



my_player = Player('Marek Markowski')
print(my_player.name)
print(my_player.goals)
print(my_player.age)
my_player.score()
my_player.score()
my_player.score()
my_player.score()
my_player.score()
print(my_player.goals)
















