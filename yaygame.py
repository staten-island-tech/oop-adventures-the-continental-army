import random

class MC:
    def __init__ (self, name, inventory = None, hunger = 100, health = 100, stamina = 100, protection = 0, living = True): #Hunger Health Stamina Shield/Armor
        self.name = name
        self.inventory = []
        self.hunger = hunger
        self.health = health
        self.stamina = stamina
        self.protection = protection
        self.living = living

    def passiveStat (self):
        self.hunger -= 3.5
        self.stamina += 2

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

        if self.protection > 20:
            self.protection = 20
        elif self.protection < 0:
            self.protection = 0
    
    def eat(self):
        self.health += 10
        self.hunger += 20
    
    def failedattack(self):
        self.stamina -= 15

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
        User.inventory.append("sword")

    def buypotion (self):
        self.money -= self.potion
        User.inventory.append("potion")
        User.health += 10

    def buyfood (self):
        self.money -= self.food
        User.inventory.append("food")

    def buyarmor (self):
        self.money -= self.armor
        User.protection += 20

    def buybowandarrow (self):
        self.money -= self.bowandarrow
        User.inventory.append("bowandarrow")

class sword(MC):
    def __init__(self, damage = 80):
        self.damage = damage
    
    def swordattack(self):
        sword.damage = 65
        damage = sword.damage
        User.stamina -= 10
        self.health -= damage

    def swordbuff(self):
        sword.damage = 100
        damage = sword.damage
        User.stamina -= 15
        self.health -= damage

    def chance(self):
        p = random.randint(1,8)
        if p == 8:
            sword.swordbuff(self)
        if p >= 4:
            print("congrats you hit the cat")
            print("keep going")
            sword.swordattack(self)
        if p <= 3:
            print("you failed try another strike")
            User4.attack()
            User.failedattack()

class bowandarrow(MC):
    def __init__(self, damage = 65):
        self.damage = damage

    def bowandarrowattack(self):
        bowandarrow.damage = 65
        damage = bowandarrow.damage
        User.stamina -= 10
        self.health -= damage
    
    def chance(self):
        b = random.randint(1,9)
        if b >= 4:
            print("yay you hit the cat")
            print("choose another weapon or attack")
            bowandarrow.bowandarrowattack()
        if b <= 3:
            print("you failed try another strike ")
            User4.attack()
            User.failedattack()


class Finalboss(MC):
    def __init__(self,name4, health = 1000, stamina =  500, successful = True):
        self.name4 = name4
        self.health = health
        self.stamina = stamina
    
    def attack(self):
        self.stamina -= 40
        self.health -= 5
        User.health -= 15  

class Fluggelcat(MC):
    def __init__(self, name3, health = 250, stamina = 100, living = True):
        self.name3 = name3
        self.health = health
        self.stamina = stamina

    def attack(self):
        self.stamina -= 10
        User.health -= 10
    
    def defend(self):
        self.stamina -= 15
        self.health -= 3
    
    def reset(self, name3, health = 250, stamina = 100, living = True):
        self.name3 = name3
        self.health = health
        self.stamina = stamina
    
class Guild(MC):
    def __init__(self, money = 1000000):
        self.money = money

    def payment1(self):
        User2.money += 500
    
    def payment2(self):
        User2.money += 1000
    
    def payment3(self):
        User2.money += 4000
    
    def deduction(self):
        User2.money -= 400

    def quest1(self):
        print("You go north and you find the entrance to the portal, without hesitating you fall in. Once you're there you see a large furry rock, you feel it and suddenly it sits up. It's the Fluggelcat. Time to defeat him. Starting battle in 3 2 1...")
    
    def quest2(self):
        print("You need to go save penguini from the orca, as you cross the icey waters you feel an ominous")

    def quest3(self):
        print("You are told to get the golden shell of the turtle but to get to the turtle shell you must fight Mr.Whalen. You enter the portal and you see a cave. You enter it and the ground starts shaking. It's Mr.Whalen! This is it! ")
print("You’re walking across the street trying to figure out how to pay your debts to the loan sharks when you walk into the street and get hit by a truck. You wake up to see you’re trapped in a black space with nobody there, then a message on a screen pops up and it says “Teleporting in 3..2..1”. ")
name = input(f"What is your name?")
User = MC(name)
User2 = SHOP(name)
User3 = Guild(name)
User4 = Fluggelcat(name)
User6 = Finalboss(name)
User7 = sword(name)
print("You've found a chest by your foot... (+500 gold)")

while User.living == True:
    print("1.) Show stats")
    print("2.) Go on a quest | Note: you must have certain weapons in order to be able to go on certain quests")
    print("3.) Eat")
    print("4.) Go shopping")
    Userinput = input(f"What do you wanna do now {User.name}?")
    Userinput = Userinput.lower()
    User2.inflation()
    User.passiveStat()
    User.maxmin()
    User.warnings()
    if User.health == 0 or User.hunger == 0 or User2.money <= -1000:
        User.living = False
    if '1' in Userinput:
        print(f"{User.hunger} hunger")
        print(f"{User.health} health")
        print(f"{User.stamina} stamina")
        print(f"{User2.money} gold")
        print(f"{User.protection} armor")
        print(f"{User.inventory}, these are your items")
    elif '3' in Userinput:
        if "food" in User.inventory:
            User.eat()
            User.inventory.remove("food")
        elif "food" not in User.inventory:
            print("Go back to the shop to purchase some food")
    elif '4' in Userinput:
        print(f"1.) A sword for {User2.sword}")
        print(f"2.) A bowandarrow for {User2.bowandarrow}")
        print(f"3.) Food for {User2.food}")
        print(f"4.) A potion for {User2.potion}")
        print(f"5.) Armor for {User2.armor}")
        Userinput2 = input(f"What would you like to buy?")
        if '1' in Userinput2:
            User2.buysword()
        elif '4' in Userinput2:
            User2.buypotion()
        elif '3' in Userinput2:
            User2.buyfood()
        elif '5' in Userinput2:
            User2.buyarmor()
        elif '2' in Userinput2:
            User2.buybowandarrow()
        print(f"You have {User2.money} gold left")
    elif '2' in Userinput:
        if User.inventory == []:
            print("you need to buy some weapons first")
        else:
            print("1.) For this task you must venture north and slay the Fluggelcat")
            print("2.)")
            print("3.)")
            Userinput3 = input("There are three portals available")
            if '1' in Userinput3:
                Userinput4= input("1.) For this task you must venture north and slay the Fluggelcat. Do you accept the quest or no?")
                if 'yes' in Userinput4:
                    User3.quest1()
                    fight1 = input("the fluggelcat is attacking. do you fight or run?")
                    if User.health <= 25:
                        print(f"{name} is {User.health} you should retreat ")
                    if "fight" in fight1:
                        while User4.health >= 0:
                            attack1 = input("what weapon will you use your sword or your bow and arrow?")
                            if "sword" in attack1:
                                if "sword" not in User.inventory:
                                    print("you don't have that weapon use something else")
                                    print(f"{User.inventory}")
                            if "bowandarrow" in attack1:
                                if "bowandarrow" not in User.inventory:
                                    print("you don't have that weapon use something else")
                                    print(f"{User.inventory}")
                            if "sword" in attack1:
                                if "sword" in User.inventory:
                                    sword.chance(User4)
                            if "bowandarrow" in attack1:
                                if "bowandarrow" in User.inventory:
                                    b = random.randint(1,8)
                                    if b >= 10:
                                        bowandarrow.bowandarrowattack()
                                    if b <= 9:
                                        User.failedattack()
                            print(f"{User4.health}") 
                    if User4.health <= 0:
                        print("congrats he is dead go back to the guild to claim your reward")
                        User3.payment1()
                        User4.reset()
            elif 'portal2' in Userinput2:
                Userinput4 = input("2.) For this task you will have to travel south and save the Penguini from the portal. Will you accept the quest or no?")
                if 'yes' in Userinput4:
                    User3.quest2()
            elif 'portal3' in Userinput2:
                Userinput3 = input("3.) For this task you will be going north-east to find the shell of the golden turtle. Do you accept the quest or no?")
                if 'yes' in Userinput3:
                    User3.quest3()
                while "yes" in Userinput2:
                    User6.attack
    
