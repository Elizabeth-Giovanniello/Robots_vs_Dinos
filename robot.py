class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
        self.health = 100 #COME BACK AND ADJUST THIS AS NEEDED

    def attack(self, dino):
        pass

    def receive_damage(self, damage_points):
        self.health -= damage_points
