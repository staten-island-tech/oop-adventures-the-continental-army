class MC:
    def __init__ (self, name, inventory = None, hunger = 100, health = 100, stamina = 100, damage = 10, protection = 0, money = 500, living = True): #Hunger Health Stamina Shield/Armor
        self.name = name
        self.inventory = inventory
        self.hunger = hunger
        self.health = health
        self.stamina = stamina
        self.damage = damage
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
        
        if self.damage < 0:
            self.damage = 0

        if self.protection > 20:
            self.protection = 20
        elif self.protection < 0:
            self.protection = 0

class SHOP:
    def __init__ (self, name2, sword = 75, potion = 40, food = 15, armor = 75, bowandarrow = 50):
        self.name2 = name2
        self.sword = sword
        self.potion = potion
        self.food = food
        self.armor = armor
        self.bowandarrow = bowandarrow

    def inflation (self):
        self.sword += 1
        self.potion += 1
        self.food += 1
        self.armor += 1
        self.bowandarrow += 1

    def buysword (self):
        self.__money -= self.sword
        self.damage += 920

    def buypotion (self):
        self.__money -= self.potion

    def buyfood (self):
        self.__money -= self.food

    def buyarmor (self):
        self.__money -= self.armor
        self.protection += 16

    def buybowandarrow (self):
        self.__money -= self.bowandarrow


print("You’re walking across the street trying to figure out how to pay your debts to the loan sharks when you walk into the street and get hit by a truck. You wake up to see you’re trapped in a black space with nobody there, then a message on a screen pops up and it says “Teleporting in 3..2..1”. ")
name = input(f"What is your name?")
User = MC(name)
User2 = SHOP(name)

while User.living == True:
    Userinput = input(f"What do you wanna do now little boy?")
    Userinput = Userinput.lower()
    if User.health == 0 or User.hunger == 0 or User.money <= -100:
        User.living = False
    if 'shop' in Userinput:
        User2.inflation()
        User.passiveStat()
        User.maxmin()
        User.warnings()
        print(f"{User.hunger} hunger")
        print(f"{User.health} health")
        print(f"{User.stamina} stamina")
        print(f"{User.money} money")
        print(f"{User.protection} armor")
        Userinput2 = input(f"Would you like to purchase a sword for {User2.sword}, a potion for {User2.potion}, food for {User2.food}, armor for {User2.armor}, or a bow & arrow for {User2.bowandarrow}?")
        if 'buysword' in Userinput2:
            User2.buysword()
