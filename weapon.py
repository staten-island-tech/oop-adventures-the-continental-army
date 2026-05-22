class Weapons:
   def __init__(self, sword, bowandarrow, potion, axe):
        self.sword = sword
        self.bowandarrow = bowandarrow
        self.potion = potion
        self.axe = axe
    
class sword(Weapons):
    def __init__(self,level, damage):
        self.level = level
        self.damage = damage
    
    def swordattack(self):
        self.stamina -= 10
       
        
