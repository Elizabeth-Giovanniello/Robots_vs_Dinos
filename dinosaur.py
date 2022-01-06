import random

class Dinosaur:

    def __init__(self, name, attack_power, attacks):
        self.name = name
        self.health = 100
        self.attack_power = attack_power
        self.energy_level = 100
        self.attack_options = attacks #added in a way to pass in a list of the dinosaur's attack options so we are only dealing with the relevant list
    
    def attack(self, robot):
        self.choose_attack()    #before each attack, user has the option to select which attack the dinosaur uses
        if self.energy_level < self.attack_power:   
            partial_attack_power = self.energy_level
            robot.health -= partial_attack_power      #this way you can't inflict more damage than you have energy for
            self.energy_level -= partial_attack_power
            #description for low-energy attacks, when attacker lacks the energy for a successful attack but isn't yet completely drained
            print(f"\n{self.name} is looking a little pale, a little unsteady... but it looks like he's going to try and push through, he's going in for the attack! He's made contact and-- my God, {self.name} just dropped to the floor like a load of bricks. Did he just pass out?! Wow, {robot.name} got off easy there! \n\n{self.name} did not have enough energy to complete this attack, and has collapsed from exhaustion mid-strike!")
        else:
            print(f"\n{self.name} {self.attack_script_one}{robot.name}{self.attack_script_two}")   #these descriptions are specific to a successful attack
            robot.health -= self.attack_power
            self.energy_level -= self.attack_power #their energy level reduces by the same level as their attack power, so heavier hitters need to recharge more often

    def choose_attack(self):
        print(f"\n{self.name}'s attack options are: ")
        num = 1
        for item in self.attack_options:
            print(f"{num}. {item[0].capitalize()}")   #printing a numbered list of options for the user
            num += 1
        user_choice = input(f"\nEnter the number of the attack you want {self.name} to use for this round. Enter any other character for an attack to be randomly assigned. ")
        if user_choice.isdigit() and int(user_choice) > 0 and int(user_choice) <= len(self.attack_options):
            attack_index = int(user_choice) - 1
            self.attack_name = self.attack_options[attack_index][0]
            self.attack_script_one = self.attack_options[attack_index][1]
            self.attack_script_two = self.attack_options[attack_index][2]
        else:
            attack_selection = random.choice(self.attack_options)
            self.attack_name = attack_selection[0]
            self.attack_script_one = attack_selection[1]
            self.attack_script_two = attack_selection[2]
    
    def power_nap(self):    #replenishes a dino's energy level after it has been completely drained
        self.energy_level = 100

  