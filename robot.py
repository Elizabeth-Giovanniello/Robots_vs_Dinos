from weapon import Weapon

import random

class Robot:
    def __init__(self, name, weapon_list):
        self.name = name
        self.weapon = None
        self.health = 100
        self.weapon_options = weapon_list 

    def attack(self, dino):
        print(f"{self.name} has attacked {dino.name} with {self.weapon.name}!")
        if self.weapon.name == "mind control":
            print(f"{self.name} is using its mind control to make {dino.name} attack itself! That's gotta sting!") #come back to this later, as we add in more options for dinosaur attacks and the energy/power drain component, we can make this more complicated
            dino.health -= dino.attack_power
        else:
            dino.health -= self.weapon.attack_power
            
    def choose_weapon(self):
        print(f"Now that you have chosen {self.name} as one of your robot champions, you must choose its weapon from the following options: ")
        self.num = 1
        for item in self.weapon_options:
            print(f"{self.num}. {item[0].capitalize()}")
            self.num += 1
        self.user_choice = input("Enter the number of the weapon you want your chosen robot champion to bear. Enter any other character for a weapon to be randomly assigned. ")
        if int(self.user_choice) > 0 and int(self.user_choice) <= len(self.weapon_options):
            self.weapon_index = int(self.user_choice) - 1
            self.weapon = Weapon(self.weapon_options[self.weapon_index][0], self.weapon_options[self.weapon_index][1])
        else:
            self.weapon = Weapon(random.choice(self.weapon_options))
        print(f"{self.name} will be using {self.weapon.name} as its weapon. ")










