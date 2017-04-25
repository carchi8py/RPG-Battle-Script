import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

class Person:
    def __init__(self, hp, mp, atk, df, magic):
        #our max hit points
        self.maxhp = hp
        #our current hit point
        self.hp = hp
        #our max magic points
        self.maxmp = mp
        #our current magic points
        self.mp = mp
        #low attack
        self. atkl = atk - 10
        #high attack
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generate_damage(self):
        """
        Generates a random damage
        :return: a random damage number
        """
        return random.randrange(self.atkl, self.atkh)