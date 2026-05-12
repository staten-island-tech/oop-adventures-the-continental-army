class MC:
    def __init__ (self, name, inventory = None, hunger = 100, health = 100, stamina = 100, damage = 10, protection = 0, living = True): #Hunger Health Stamina Shield/Armor
        self.name = name
        self.inventory = inventory
        self.hunger = hunger
        self.health = health
        self.stamina = stamina
        self.damage = damage
        self.protection = protection
        self.living = living

    def passiveStat (self):
        self.hunger -= 5
        self.stamina += 5

    def warnings (self):
        if self.hunger == 25:
            print(f"You are starving.")
            self.health -= 8.5
        elif self.hunger == 10:
            print(f"Your insides are burning.")
            self.health -= 19
        elif self.hunger <= 0:
            print(f"You died.")

        if self.health == 25:
            print(f"Your starting to bleed out.")
        elif self.health == 10:
            print(f"You are dying.")
        elif self.health <= 0:
            print(f"You died.")

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

class SHOP(MC):
    def __init__ (self, name2, money = 500, sword = 75, potion = 40, food = 15, armor = 75, bowandarrow = 50):
        self.name2 = name2
        self.money = money
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
        self.money -= self.sword

    def buypotion (self):
        self.money -= self.potion
        self.health += 35

    def buyfood (self):
        self.money -= self.food
        self.hunger += 30

    def buyarmor (self):
        self.money -= self.armor
        self.protection += 16

    def buybowandarrow (self):
        self.money -= self.bowandarrow
        self.damage += 90

print("You’re walking across the street trying to figure out how to pay your debts to the loan sharks when you walk into the street and get hit by a truck. You wake up to see you’re trapped in a black space with nobody there, then a message on a screen pops up and it says “Teleporting in 3..2..1”. ")
name = input(f"What is your name?")
User = MC(name)
User2 = SHOP(name)
print("You've found a chest by your foot... (+500 gold)")

while User.living == True:
    Userinput = input(f"What do you wanna do now {User.name}?")
    Userinput = Userinput.lower()
    User2.inflation()
    User.passiveStat()
    User.maxmin()
    User.warnings()
    if User.health == 0 or User.hunger == 0 or User2.money <= -1000:
        User.living = False
    elif 'shop' in Userinput:
        print(f"{User.hunger} hunger")
        print(f"{User.health} health")
        print(f"{User.stamina} stamina")
        print(f"{User2.money} gold")
        print(f"{User.protection} armor")
        print(f"")
        Userinput2 = input(f"Would you like to purchase a sword for {User2.sword}, a potion for {User2.potion}, food for {User2.food}, armor for {User2.armor}, or a bow & arrow for {User2.bowandarrow}? Type 'cancel' to rethink your choices...")
        if 'buysword' in Userinput2:
            User2.buysword()
            User.damage += 20
        elif 'buypotion' in Userinput2:
            User2.buypotion()
        elif 'buyfood' in Userinput2:
            User2.buyfood()
        elif 'buyarmor' in Userinput2:
            User2.buyarmor()
        elif 'buybowandarrow' in Userinput2:
            User2.buybowandarrow()