class MC:
    def __init__ (self, name, hunger = 100, health = 100, stamina = 100, protection = 20, living = True): #Hunger Health Stamina Shield/Armour
        self.name = name
        self.hunger = hunger
        self.health = health
        self.stamina = stamina
        self.protection = protection
        self.living = living

    def statDec (self):
        self.hunger -= 5

    def maxmin (self):
        if self.hunger > 100:
            self.hunger = 100
        elif self.hunger < 0:
            self.hunger = 0
        
        if self.health > 100:
            self.health = 100
        elif self.health < 0:
            self.health = 0

        if self.stamina > 100:
            self.stamina = 100
        elif self.stamina < 0:
            self.stamina = 0

        if self.protection > 20:
            self.protection = 20
        elif self.protection < 0:
            self.protection = 0