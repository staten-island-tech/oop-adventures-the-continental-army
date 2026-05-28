from yaygame import MC
    
class sword:
    def __init__(self, damage = 65):
        self.damage = damage
    
    def swordattack(self):
        MC.stamina -= 10
        self.health -= self.damage


