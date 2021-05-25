# class Temple():
#     def _init_(self,name=None):
#         self.hp = 200
#         self.x = 20
#         self.y= 50
#         self.name=name
    
#     def double_x(self):
#         self.x = 2*self.x
        
#     def double_y(self): 
#         self.y = 2*self.y
        
#     def ChangeName(self, newname):
#         self.name = newname

# temple1=Temple()
    
# print(temple1.x)
import random
class Fighter:
    # Enter code below
def _init_(self):
    self.level=1
    self.hp=100
    self.mp=20
    self.strength=20
    self.armor=60
    
def attack(self):
    return random.readint(self.strength/2, self.strength)

def takeDamage(self,amount):
    self.hp += (-self.armor/100)*amount
    
    
def level_up(self):
    self.strength += self.strength*0.2
    self.armor += self.armor*0.2
    self.hp += 30
    self.level += 1

fighter1 = Fighter()
