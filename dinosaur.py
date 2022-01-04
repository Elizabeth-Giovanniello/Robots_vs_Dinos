import random

class Dinosaur:

    def __init__(self, name, attack_power, attacks):
        self.name = name
        self.health = 100
        self.attack_power = attack_power
        self.attack_options = attacks
    
    def attack(self, robot):
        self.choose_attack()
        print(f"{self.name} has attacked {robot.name} by {self.attack_name}!")
        robot.health -= self.attack_power
    
    def choose_attack(self):
        print(f"{self.name}'s attack options are: ")
        self.num = 1
        for item in self.attack_options:
            print(f"{self.num}. {item.capitalize()}")
            self.num += 1
        self.user_choice = input(f"Enter the number of the attack you want {self.name} to use for this round. Enter any other character for an attack to be randomly assigned. ")
        if int(self.user_choice) > 0 and int(self.user_choice) <= len(self.attack_options):
            self.attack_index = int(self.user_choice) - 1
            self.attack_name = self.attack_options[self.attack_index]
        else:
            self.attack_name = random.choice(self.attack_options)

  