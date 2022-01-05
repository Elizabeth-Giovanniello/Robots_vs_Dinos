import random

class Dinosaur:

    def __init__(self, name, attack_power, attacks):
        self.name = name
        self.health = 100
        self.attack_power = attack_power
        self.energy_level = 100
        self.attack_options = attacks #added in a way to pass in a list of the dinosaur's attack options so we are only dealing with the relevant list
    
    def attack(self, robot):
        self.choose_attack()
        print(f"{self.name} has attacked {robot.name} by {self.attack_description}!") # TODO possibly fix this wording so it makes more sense
        if self.energy_level < self.attack_power:
            partial_attack_power = self.energy_level
            robot.health -= partial_attack_power      #this way you can't inflict more damage than you have energy for
            self.energy_level -= partial_attack_power
            print(f"{self.name} did not have enough energy to complete this attack, and has collapsed from exhaustion mid-strike!")
        else:
            robot.health -= self.attack_power
            self.energy_level -= self.attack_power #their energy level reduces by the same level as their attack power, so heavier hitters need to recharge more often

    def choose_attack(self):
        print(f"{self.name}'s attack options are: ")
        num = 1
        for item in self.attack_options:
            print(f"{num}. {item[0].capitalize()}")   #printing a numbered list of options for the user
            num += 1
        user_choice = input(f"\nEnter the number of the attack you want {self.name} to use for this round. Enter any other character for an attack to be randomly assigned. ")
        if int(user_choice) > 0 and int(user_choice) <= len(self.attack_options):
            attack_index = int(user_choice) - 1
            self.attack_name = self.attack_options[attack_index][0]
            self.attack_description = self.attack_options[attack_index][1]
        else:
            attack_selection = random.choice(self.attack_options)
            self.attack_name = attack_selection[0]
            self.attack_description = attack_selection[1]
    
    def power_nap(self):
        self.energy_level = 100

  