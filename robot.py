class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
        self.health = 100 #COME BACK AND ADJUST THIS AS NEEDED

    def attack(self, dino):
        print(f"{self.name} has attacked {dino} with {self.weapon.name}!")
        return self.weapon.attack_power

    #def receive_damage(self, damage_points):
        #self.health -= damage_points
        #might be making this method obsolete by adding it directly into the attack method