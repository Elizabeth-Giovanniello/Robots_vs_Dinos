class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power
    
    def attack(self, robot):
        print(f"{self.name} has attacked {robot.name}!")
        robot.health -= self.attack_power

  