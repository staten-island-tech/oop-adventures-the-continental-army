class MC:
    def __init__ (self, name, inventory, hunger = 100, health = 100, stamina = 100, protection = 0, money = 0, living = True): #Hunger Health Stamina Shield/Armor
        self.name = name
        self.inventory = inventory
        self.hunger = hunger
        self.health = health
        self.stamina = stamina
        self.protection = protection
        self.money = money
        self.living = living

    def passiveStat (self):
        self.hunger -= 5
        self.stamina += 5

    def warnings (self):
        if self.hunger <= 25:
            print(f"{self.name} is starving.")
        if self.health <= 25:
            print(f"{self.name} is bleeding out.")

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

class SHOP:
    def __init__ (self, sword = 75, potion = 40, food = 15, armor = 75, bowANDarrow = 50):
        self.sword = sword
        self.potion = potion
        self.food = food
        self.armor = armor
        self.bowANDarrow = bowANDarrow

    def buy (self):
        self.__money -= self.armor


print("copy that intro msg uhdehjdgfkl")
name = input("What is your name?")
User = MC(name)

while User.living == True:
    Userinput = input("uiuirtldkhl")
    Userinput = Userinput.lower()
    if '' in Userinput:
        User.passiveStat()
        User.maxmin()
        User.warnings()
        print(f"{User.hunger} hunger")
        print(f"{User.health} health")
        print(f"{User.stamina} stamina")
        print(f"{User.money} money")
        print(f"{User.protection} armor")