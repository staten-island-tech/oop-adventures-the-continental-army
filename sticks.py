class MC:
    def __init__ (self, name, inventory = None, hunger = 100, health = 100, stamina = 100, damage = 10, protection = 0, money = 250, living = True): #Hunger Health Stamina Shield/Armor
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
        self.hunger -= 2
        self.stamina += 5

    def warnings (self):
        if self.hunger == 25:
            print(f"You are starving.")
            self.health -= 8.5
        elif self.hunger == 10:
            print(f"Your insides are burning.")
            self.health -= 19

        if self.health == 25:
            print(f"Your starting to bleed out.")
        elif self.health == 10:
            print(f"You are dying.")

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
    
    def block(self):
        self.protection -= 5
        self.stamina -= 10

    def attack(self):
        self.stamina -= 10

class SHOP(MC):
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
        User.money -= self.sword
        User.damage += 20

    def buypotion (self):
        User.money -= self.potion
        User.health += 50

    def buyfood (self):
        User.money -= self.food
        User.hunger += 30

    def buyarmor (self):
        User.money -= self.armor
        User.protection += 16

    def buybowandarrow (self):
        User.money -= self.bowandarrow
        User.damage += 90

class Hunter(MC):
    def __init__(self, name3, health, stamina = 100, living = True):
        self.name3 = name3
        self.health = health
        self.stamina = stamina

    def attack1(self):
        self.stamina -= 10
        User.health -= 10
    
    def attack2(self):
        self.stamina -= 10
        User.health -= 20

    def attacked(self):
        self.health -= User.damage

class Guild(MC):
    def __init__(self, money = 1000000):
        self.money = money

    def payment1():
        User.money += 500

    def payment2():
        User.money += 2000

    def payment3():
        User.money += 4000

    def deduction():
        quest1 -= 45
        quest2 -= 450
        quest3 -= 750

print("You’re walking across the street trying to figure out how to pay your debts to the loan sharks when you walk into the street and get hit by a truck. You wake up to see you’re trapped in a black space with nobody there, then a message on a screen pops up and it says “Teleporting in 3..2..1”. ")
print("You’ve awoken in an unfamiliar, damp place…as you come to consciousness, you realize this isn’t your city. The area is lit only by the soft glow of lanterns. The ground beneath you seems to swallow you in—a rush of footsteps run past where you lay, ‘Follow me, this way! The portal is highly unstable!’ This world…is not your own… DUN DUN DUN.")
name = input(f"What is your name?")
User = MC(name)
User2 = SHOP(name)
User3 = Guild(name)
User4 = Hunter(name)
print("You've found a chest by your foot... (+250 gold)")

while User.living == True:
    Userinput = input(f"What do you wanna do now {User.name}?")
    Userinput = Userinput.lower()
    User2.inflation()
    User.passiveStat()
    User.maxmin()
    User.warnings()
    if User.health == 0:
        print("You're bad at this...how did you even manage to die?")
        User.living = False
    elif User.hunger == 0:
        print("You died of starvation! AHahhahahagahah.")
        User.living = False
    elif User.money <= -500:
        print("You have fallen into the abyss of no return. You shall now work forever for the evil debt collecter for the rest of your undead days...")
        User.living = False
    elif 'stats' in Userinput:
        print(f"{User.hunger} hunger")
        print(f"{User.health} health")
        print(f"{User.stamina} stamina")
        print(f"{User.money} gold")
        print(f"{User.protection} armor")
        print(f"{User.damage} damage")
    elif 'shop' in Userinput:
        Userinput2 = input(f"Would you like to purchase a sword for {User2.sword}, a potion for {User2.potion}, food for {User2.food}, armor for {User2.armor}, or a bow & arrow for {User2.bowandarrow}? Type 'cancel' to rethink your choices...")
        Userinput2 = Userinput2.lower()
        if 'buysword' in Userinput2:
            User2.buysword()
        elif 'buypotion' in Userinput2:
            User2.buypotion()
        elif 'buyfood' in Userinput2:
            User2.buyfood()
        elif 'buyarmor' in Userinput2:
            User2.buyarmor()
        elif 'buybowandarrow' in Userinput2:
            User2.buybowandarrow()
    elif 'quests' in Userinput:
        Userinput2 = input(f"There are three portals available, which would you like, the first one, the second one, or the third one?")
        Userinput2 = Userinput.lower()
        if 'portal1' in Userinput2:
            Userinput3 = input("1.) For this task you must venture north and slay the Fluggelcat. Do you accept the quest?")
            Userinput3 = Userinput3.lower()
            while 'yes' in Userinput3:
                print("You go north and you find the entrance to the portal, without hesitating you fall in. Once you're there you see a large furry rock, you feel it and suddenly it sits up. It's the Fluggelcat. Prepare to defeat him. Commencing the battle in 3...2...1... BEGIN!")
                fight1 = input("The Fluggelcat is attacking. Do you fight, block, or run?")
                fight1 = fight1.lower()
                if "block" in fight1:
                    User.block()
                elif "fight" in fight1:
                    User.attack()
                    User4.attacked()
                    User4.attack1()
                elif "run" in fight1:
                    print("You coward...the Fluggelcat chases after you and strikes again!")
                if User4.health > 0:
                     print(f"The Fluggelcat has {User4.health}")
                elif User4.health <= 0:
                    print(f"Congratulations {User.name}! You've defeated the Fluggelcat in a vicious battle. The Guild awards you handsomely!")
                    User3.payment1
                    break
        elif 'portl2' in Userinput2:
            Userinput3 = input("2.) For this task you will have to travel south and save Penguini from the portal. Will you accept the quest or decline like the cowardly man you are?")
            Userinput3 = Userinput3.lower()
            while 'yes' in Userinput3:
                print("You travel down south to Antarctica. Inside the portal there lays a hidden beast within the icy waters...a smooth black and white figure emerges from the ocean. He spans a whole 26 feet! I wish you luck...traveller. Commencing the battle in 3...2...1... BEGIN!")
                fight1 = input("Nandu strikes fiercely. Do you fight, block, or run?")
                fight1 = fight1.lower()
                if "block" in fight1:
                    User.block()
                elif "fight" in fight1:
                    User.attack()
                    User4.attacked()
                    User4.attack2()
                elif "run" in fight1:
                    print("You coward...the Fluggelcat chases after you and strikes again!")
                if User4.health > 0:
                     print(f"Nandu has {User4.health}")
                elif User4.health <= 0:
                    print(f"Congratulations {User.name}! You've defeated Nandu in battle. How does it feel to kill an innocent Orca who is merely trying to survive? The Guild awards you...noble sir.")
                    User3.payment2
                    break

        elif 'portal3' in Userinput:
            Userinput3 = input("3.) For this task you will be going north-east to find the shell of the golden turtle. Do you accept the quest or no?")
            if 'yes' in Userinput3:
                User3.quest3()