from weapon import Weapon

import random

class Robot:
    def __init__(self, name, weapon_list):
        self.name = name
        self.weapon = None
        self.health = 100
        self.power_level = 100
        # * Changed out weapon to be weapon list for bonus story
        self.weapon_options = weapon_list
      

    def attack(self, dino):
        print(f"{self.name} has attacked {dino.name} with {self.weapon.name}!")
        if self.weapon.name == "mind control":
            print(f"{self.name} is using its mind control to make {dino.name} attack itself! That's gotta sting!")  #making the mind control weapon have the opponent attack itself
            dino.health -= dino.attack_power  #the opponent's own attack power will be used against it
            dino.energy_level -= dino.attack_power #both the robot and dinosaur will lose energy/power from this
        else:
            dino.health -= self.weapon.attack_power
        self.power_level -= self.weapon.attack_power
            
    def choose_weapon(self):
        print(f"\nNow that you have chosen {self.name} as one of your robot champions, you can choose its weapon from the following options: ")
        num = 1
        for item in self.weapon_options:
            print(f"{num}. {item[0].capitalize()}")
            num += 1
        user_choice = input("\nEnter the number of the weapon you want your chosen robot champion to bear. Enter any other character for a weapon to be randomly assigned. ")
        if int(user_choice) > 0 and int(user_choice) <= len(self.weapon_options):
            weapon_index = int(user_choice) - 1
            self.weapon = Weapon(self.weapon_options[weapon_index][0], self.weapon_options[weapon_index][1])
        else:
            self.weapon = random.choice(self.weapon_options)
            self.weapon = Weapon(self.weapon[0], self.weapon[1])
        print(f"{self.name} will be using {self.weapon.name} as its weapon. ")

    def recharge_batteries(self):
        self.power_level = 100










