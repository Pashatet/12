class Hero():
    """Class to create hero for game"""
    def __init__(self, name, level, race) -> None:
        """Initiate our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100
    
    def show_here(self):
        """"print all parameters"""
        discription = (self.name + ' level is: ' + str(self.level) + ' Race is: ' + self.race + ' health hero is: ' + str(self.health))
        print(discription)

    def level_up(self):
        """upgrate level of hero"""
        self.level += 1

    def move(self):
        print('Hero ' + self.name + ' start moving... ')

    def set_health(self, new_health):
        self.health=new_health

# -----------new class--------
class SuperHero(Hero):
    """Class to create super hero"""
    def __init__(self, name, level, race, magiclevel) -> None:
        """Initiate our super hero"""
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.magic = 100

    def makemagic(self):
        """Upgrate magic of super hero"""
        self.magic -= 10
    
    def show_here(self):
        """"print all parameters"""
        discription = (self.name + ' level is: ' + str(self.level) + ' Race is: ' + self.race + ' health hero is: ' + str(self.health) + ' magic is:' + str(self.magic))
        print(discription)