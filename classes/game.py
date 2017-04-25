import random

class bcolors:
    """
    bcolors is a class with the terminal colors we are going to be using
    """
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
    """
    Person is a class with our hero
    """
    def __init__(self, hp, mp, atk, df, magic):
        """
        Set up our here
        :param hp: The heroes HP
        :param mp: The heroes mp
        :param atk: The Heroes attack
        :param df: The heroes defence
        :param magic: the heroes magic
        """
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

    def generate_spell_damage(self, i):
        """
        Generate spell damage
        :param i: The spell the player is using
        :return: the damage the spell did
        """
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)

    def take_damage(self, dmg):
        """
        Function to tell how much damage we took
        :param dmg: the damage we've taken
        :return: How much HP the player has left
        """
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp