class MC:
    def __init__ (self, name, inventory = None, hunger = 100, health = 100, stamina = 100, damage = 10, protection = 0, money = 0, living = True): #Hunger Health Stamina Shield/Armor
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
        self.health += 3

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
        self.sword += 5
        self.potion += 5
        self.food += 5
        self.armor += 5
        self.bowandarrow += 5

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

class FLUGGELCAT(MC):
    def __init__(self, name3, health = 250, stamina = 100):
        self.name3 = name3
        self.health = health
        self.stamina = stamina

    def attack(self):
        self.stamina -= 10
        User.health -= 10

    def attacked(self):
        self.health -= User.damage

    def statreset(self):
        self.health = 250
        self.stamina = 100

class NANDU (MC):
    def __init__(self, name4, health = 2190, stamina = 500):
        self.name4 = name4
        self.health = health
        self.stamina = stamina

    def attack(self):
        self.stamina -= 10
        User.health -= 15

    def attacked(self):
        self.health -= User.damage

    def statreset(self):
        self.health = 2190
        self.stamina = 500

class ODIN (MC):
    def __init__(self, name5, health = 100000000, stamina = 10000):
        self.name5 = name5
        self.health = health
        self.stamina = stamina

    def attack(self):
        self.stamina -= 10
        User.health -= 40

    def attacked(self):
        self.health -= User.damage

    def statreset(self):
        self.health = 100000000
        self.stamina = 10000

class GUILD(MC):
    def payment1(self):
        User.money += 500

    def payment2(self):
        User.money += 2000

    def payment3(self):
        User.money += 10000

    def deduction(self):
        quest1 -= 45
        quest2 -= 450
        quest3 -= 750

print("You’re walking across the street trying to figure out how to pay your debts to the loan sharks when you walk into the street and get hit by a truck. You wake up to see you’re trapped in a black space with nobody there, then a message on a screen pops up and it says “Teleporting in 3..2..1”. ")
print("You’ve awoken in an unfamiliar, damp place…as you come to consciousness, you realize this isn’t your world. The area is lit only by the soft glow of lanterns. The ground beneath you seems to swallow you in. A rush of footsteps run past where you lay, ‘Follow me, this way! The portal is highly unstable!’ This world…is not your own… DUN DUN DUN.")
name = input("Hello traveller! What is your name?")
User = MC(name)
Shop = SHOP(name)
Guild = GUILD(name)
Fluggelcat = FLUGGELCAT(name)
Nandu = NANDU(name)
Odin = ODIN(name)
print(f"Do keep in mind that this game uses no spacing for decisions! Have fun {User.name}!! Don't die! I wish you well. Bring glory to the king!")
print("You've found a chest by your foot... (+250 gold)")
User.money += 250

while User.living == True:
    Userinput = input(f"What do you wanna do now {User.name}? Shop, stats or quests...make your choice wisely!")
    Userinput = Userinput.lower()
    Shop.inflation()
    User.passiveStat()
    User.maxmin()
    User.warnings()
    if User.hunger == 0:
        print("You died of starvation! AHahhahahagahah!!")
        User.living = False
    elif User.money <= 0:
        print("You have fallen into the abyss of no return. You shall now work forever for the evil debt collecter for the rest of your dead days...")
        User.living = False
    elif 'kms' in Userinput:
        print(f"{User.name}? Hello? Are you still there? There's so much left to explore. Don't leave so soon, dear traveller...you are always welcome back.")
        User.living = False
    elif 'ilynarratorsenpai' in Userinput:
        print(f"{User.name}, what is the meaning of this? I will NEVER reciprocate such...emotion towards you..of all people.")
        User.living = False
    elif 'stats' in Userinput:
        print(f"{User.hunger} hunger")
        print(f"{User.health} health")
        print(f"{User.stamina} stamina")
        print(f"{User.money} gold")
        print(f"{User.protection} armor")
        print(f"{User.damage} damage")
    elif 'shop' in Userinput:
        Userinput = input(f"Would you like to purchase a sword for {Shop.sword}, a potion for {Shop.potion}, food for {Shop.food}, armor for {Shop.armor}, or a bow & arrow for {Shop.bowandarrow}? (ex: 'buysword') Type 'cancel' to rethink your choices...")
        Userinput = Userinput.lower()
        if 'buysword' in Userinput:
            Shop.buysword()
        elif 'buypotion' in Userinput:
            Shop.buypotion()
        elif 'buyfood' in Userinput:
            Shop.buyfood()
        elif 'buyarmor' in Userinput:
            Shop.buyarmor()
        elif 'buybowandarrow' in Userinput:
            Shop.buybowandarrow()
    elif 'quests' in Userinput:
        Userinput = input(f"There are three portals available, which would you like Portal One, Portal Two, or Portal Three? (ex: 'portalone')")
        Userinput = Userinput.lower()
        if 'portalone' in Userinput:
            Userinput = input("1.) For this task you must venture north and slay the Fluggelcat. Do you accept the quest? Type 'accept'.")
            Userinput = Userinput.lower()
            Fluggelcat.statreset()
            if 'accept' in Userinput:
                fight1 = input("You go north and you find the entrance to the portal, without hesitating you fall in. Once you're there you see a large furry rock, you feel it and suddenly it sits up. It's the Fluggelcat. Prepare to defeat him. Are you ready? Type 'ready'.")
                fight1 = fight1.lower()
                while 'ready' in fight1:
                    fight = input("The Fluggelcat is attacking. Do you fight, block, or run?")
                    fight = fight.lower()
                    User.passiveStat()
                    if "block" in fight:
                        User.block()
                        Fluggelcat.attack()
                        print("Hah, you've failed to dodge the Fluggelcat's attack!")
                    elif "fight" in fight:
                        User.attack()
                        Fluggelcat.attacked()
                        Fluggelcat.attack()
                        print("You've got him! Keep it up!")
                    elif "run" in fight:
                        print("You coward...the Fluggelcat chases after you and strikes again!")
                    if Fluggelcat.health > 0 and User.health > 0:
                        print(f"The Fluggelcat has {Fluggelcat.health} health.")
                        print(f"{User.name} has {User.health} health.")
                    elif Fluggelcat.health <= 0:
                        print(f"Congratulations {User.name}! You've defeated the Fluggelcat in a vicious battle. The Guild awards you handsomely!")
                        Guild.payment1()
                        break
                    elif User.health <= 0:
                        print(f"PFFT! How did you even manage to die? HAHAHAH, you're so pathetic.")
                        User.living = False
                        break
        elif 'portaltwo' in Userinput:
            Userinput = input("2.) For this task you will have to travel south and save Penguini from the portal. Will you accept the quest or decline like the cowardly man you are? Tpe 'accept'.")
            Userinput = Userinput.lower()
            User.passiveStat()
            Nandu.statreset()
            if 'accept' in Userinput:
                fight1 = input("You travel down south to Antarctica. Inside the portal there lays a hidden beast within the icy waters...a smooth black and white figure emerges from the ocean. He spans a whole 26 feet! I wish you luck...traveller. Are you ready? Type 'ready'.")
                fight1 = fight1.lower()
                while 'ready' in fight1:
                    fight = input("Nandu strikes fiercely. Do you fight, block, or run?")
                    fight = fight.lower()
                    if "block" in fight:
                        User.block()
                        Nandu.attack()
                        print("Nunda manages to strike you with his massive flippers!! Haven't you learned anything from fighting the Fluggelcat? Do better...this never works out.")
                    elif "fight" in fight:
                        User.attack()
                        Nandu.attacked()
                        Nandu.attack()
                        print("Nice work! But do you truly wish to sacrifice an innocent life for another?")
                    elif "run" in fight:
                        print("How disgusting...you would not even try to fight for your own companion.? Nandu continues to come after you.")
                    if Nandu.health > 0 and User.health > 0:
                        print(f"Nandu has {Nandu.health} health.")
                        print(f"{User.name} has {User.health} health.")
                    elif Nandu.health <= 0:
                        print(f"Congratulations {User.name}! You've defeated Nandu in battle. How does it feel to kill an innocent Orca who is merely trying to survive? The Guild awards you...noble sire.")
                        Guild.payment2()
                        break
                    elif User.health <= 0:
                        print(f"PFFT! How did you even manage to die? HAHAHAH, you're so pathetic.")
                        User.living = False
                        break
        elif 'portalthree' in Userinput:
            Userinput = input("3.) For this task you will be going north-east to find the shell of the golden turtle. Are you sure you would like to accept this quest? Type 'accept'.")
            Userinput = Userinput.lower()
            User.passiveStat()
            Odin.statreset()
            if 'accept' in Userinput:
                fight1 = input("After many long days of travel within the expansive forest, you come across the opening of the portal. As you enter, the world becomes dark and grim...bright red eyes stare down at you. This is your final trial to bring glory to the kingdom: Kill the God of Ravens and retreive the golden shell. Are you ready? Type 'ready'.")
                fight1 = fight1.lower()
                while 'ready' in fight1:
                    fight = input("Odin, God of Ravens, sends a flock of mighty man-eating birds towards you. Do you fight, block, or run?")
                    fight = fight.lower()
                    if "block" in fight:
                        User.block()
                        Odin.attack()
                        print("The conspiracy rips your flesh apart...bit by bit. Don't you understand traveller..? You will never stop their attempts...it is futile to believe you are able.")
                    elif "fight" in fight:
                        User.attack()
                        Odin.attacked()
                        Odin.attack()
                        print(f"You managed to land a hit on him? Good job {User.name}! Although...he always strikes as well. Be careful now.")
                    elif "run" in fight:
                        print(f"My dear traveller, you will never outrun them. The conspiracy will always find you. How can you run for an eternity..? {User.name}, you will die knowing you tried.")
                    if Odin.health > 0 and User.health > 0:
                        print(f"Odin has {Odin.health} health.")
                        print(f"{User.name} has {User.health} health.")
                    elif Odin.health <= 0:
                        print(f"Congratulations {User.name}! You...you actually managed to kill him? I'm so proud of you {User.name}. You can finally return home.")
                        Guild.payment3()
                        break
                    elif User.health <= 0:
                        print(f"{User.name}...close your eyes now. I've always been so proud of you. Since the beginning, I knew you had the determination to continue. I could see it in your eyes...Rest well, {User.name}. May you be treated well in the afterlife.")
                        User.living = False
                        break