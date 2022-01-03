from weapon import Weapon

class Robot:
    def __init__(self, name, weapon_name, weapon_attack):
        self.name = name
        self.weapon = Weapon(weapon_name, weapon_attack)
        self.health = 100 #COME BACK AND ADJUST THIS AS NEEDED

    def attack(self, dino):
        print(f"{self.name} has attacked {dino} with {self.weapon.name}!")
        dino.health -= self.weapon.attack_power
        #return self.weapon.attack_power    #only necessary if we keep receive damage method

    #def receive_damage(self, damage_points):
        #self.health -= damage_points
        #might be making this method obsolete by adding it directly into the attack method