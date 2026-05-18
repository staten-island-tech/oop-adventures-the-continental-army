class MC:
    def __init__ (self, name, inventory = None, hunger = 100, health = 100, stamina = 100, damage = 10, protection = 0, living = True): #Hunger Health Stamina Shield/Armor
        self.name = name
        self.inventory = []
        self.hunger = hunger
        self.health = health
        self.stamina = stamina
        self.damage = damage
        self.protection = protection
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
    
    def block(self):
        self.protection -= 10
        self.stamina -= 10
        self.health += 10

    def attack(self):
        self.stamina -= 10
    
    def eat(self):
        self.health += 10
        self.hunger += 40

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
        User.damage += 20

    def buypotion (self):
        self.money -= self.potion
        User.damage += 20

    def buyfood (self):
        self.money -= self.food
        User.inventory.append("food")

    def buyarmor (self):
        self.money -= self.armor
        User.protection += 20

    def buybowandarrow (self):
        self.money -= self.bowandarrow
        User.damage += 20
        

class Hunter(MC):
    def __init__(self, name3, health = 250, stamina = 100, living = True):
        self.name3 = name3
        self.health = health
        self.stamina = stamina

    def attack(self):
        self.stamina -= 10
        User.health -= 10

    def attacked(self):
        self.health -= User.damage
    
    def defend(self):
        self.stamina -= 15
        self.health -= 3
    
class Guild(MC):
    def __init__(self, money = 1000000):
        self.money = money

    def payment1(self):
        User2.money += 500
    
    def payment2(self):
        User2.money += 1000
    
    def payment3(self):
        User2.money += 4000
    
    def deduction():
        User2.money -= 400

    def quest1(self):
        print("You go north and you find the entrance to the portal, without hesitating you fall in. Once you're there you see a large furry rock, you feel it and suddenly it sits up. It's the Fluggelcat. Time to defeat him. Starting battle in 3 2 1...")
    

print("You’re walking across the street trying to figure out how to pay your debts to the loan sharks when you walk into the street and get hit by a truck. You wake up to see you’re trapped in a black space with nobody there, then a message on a screen pops up and it says “Teleporting in 3..2..1”. ")
print("You’ve awoken in an unfamiliar, damp place…as you come to consciousness, you realize this isn’t your city. The area is lit only by the soft glow of lanterns. The ground beneath you seems to swallow you in—a rush of footsteps run past where you lay, ‘Follow me, this way! The portal is highly unstable!’ This world…is not your own… DUN DUN DUN.")
name = input(f"What is your name?")
User = MC(name)
User2 = SHOP(name)
User3 = Guild(name)
User4 = Hunter(name)
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
    elif 'stats' in Userinput:
        print(f"{User.hunger} hunger")
        print(f"{User.health} health")
        print(f"{User.stamina} stamina")
        print(f"{User2.money} gold")
        print(f"{User.protection} armor")
        print(f"{User.damage} damage")
    elif 'eat' in Userinput:
        if User.inventory == "food":
            User.eat
        elif User.inventory != "food":
            print("Go back to the shop to purchase some food")
    elif 'shop' in Userinput:
        Userinput2 = input(f"Would you like to purchase a sword for {User2.sword}, a potion for {User2.potion}, food for {User2.food}, armor for {User2.armor}, or a bow & arrow for {User2.bowandarrow}? Type 'cancel' to rethink your choices...")
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
        if 'portal1' in Userinput2:
            Userinput3= input("1.) For this task you must venture north and slay the Fluggelcat. Do you accept the quest or no?")
            if 'yes' in Userinput3:
                User3.quest1()
            while 'yes' in Userinput3:
                User4.attack()
                fight1 = input("the fluggelcat is attacking. do you fight, block, or run?")
                if "run" in fight1:
                    print("you are a coward go back to the guild to pay your penalty")
                    break
                elif "block" in fight1:
                    User.block()
                elif "fight" in fight1:
                    User.attack
                    User4.attacked()
                if User4.health >= 0:
                        print(f"The fluggelcat is now at {User4.health} health")
                elif User4.health <= 0:
                    User4.health = 0
                    print("congrats he is dead go back to the guild to claim your reward")
                    User3.payment1()
                    break
        elif 'portal2' in Userinput2:
            Userinput4 = input("2.) For this task you will have to travel south and save the Penguini from the portal. Will you accept the quest or no?")
            if 'yes' in Userinput4:
                User3.quest2()
        elif 'portal3' in Userinput:
            Userinput3 = input("3.) For this task you will be going north-east to find the shell of the golden turtle. Do you accept the quest or no?")
            if 'yes' in Userinput3:
                User3.quest3()
    
