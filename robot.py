from weapon import Weapon

class Robot:
    def __init__(self, name, weapon_name, weapon_attack):
        self.name = name
        self.weapon = Weapon(weapon_name, weapon_attack)
        self.health = 100 #COME BACK AND ADJUST THIS AS NEEDED

    def attack(self, dino):
        print(f"{self.name} has attacked {dino.name} with {self.weapon.name}!")
        dino.health -= self.weapon.attack_power
            



