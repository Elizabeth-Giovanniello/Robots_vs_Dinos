from fleet import Fleet
from herd import Herd

import random

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
    
    def run_game(self):
        self.display_welcome()
        self.show_dino_opponent_options()
        self.show_robo_opponent_options()
        self.battle()
        self.display_winners()

    def display_welcome(self):
        print("Welcome to the ultimate battle of the ages, where we pit the ingenuity of modern technology against the brute strength of the prehistoric era! In this no holds barred fight to the death, I give you: Robots versus Dinosaurs!")
    
    def battle(self):
        self.current_team = self.coin_flip()
        while len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) >0:
            if self.current_team == "Team Robot":
                self.robo_turn()
                self.current_team = "Team Dinosaur"
            else: 
                self.dino_turn()
                self.current_team = "Team Robot"
        if len(self.herd.dinosaurs) > 0:
            print("And that does it, folks! As the only team left standing, the dinosaurs WIN! I guess that just goes to show, modern technology has its limits.")
        elif len(self.fleet.robots) > 0: 
            print("And there you have it, folks! In the ultimate showdown between robots and dinosaurs, robots are the only ones left standing. We haven't seen a defeat this crushing since the meteor hit!")

    def dino_turn(self):
        self.attacker = random.choice(self.herd.dinosaurs)
        self.target = random.choice(self.fleet.robots)
        print(f"This round we have {self.attacker.name} attacking {self.target.name}. ")
        self.attacker.attack(self.target)
        if self.target.health <= 0:
            self.fleet.robots.remove(self.target)
            print(f"Following the last attack, {self.target.name}'s circuitry has taken too much damage, and is no longer functional. {self.target.name} is no longer part of this fleet.")

    def robo_turn(self):
        self.attacker = random.choice(self.fleet.robots)
        self.target = random.choice(self.herd.dinosaurs)
        print(f"This round we have {self.attacker.name} attacking {self.target.name}. ")
        self.attacker.attack(self.target)
        if self.target.health <= 0:
            self.herd.dinosaurs.remove(self.target)
            print(f"Following the last attack, {self.target.name} has been too severely wounded, and has died. {self.target.name} is no longer part of this herd.")

    def show_dino_opponent_options(self):
        self.herd.create_herd()
        print(f"Representing Team Dinosaur we have {self.herd.dino_one.name}, {self.herd.dino_two.name}, and {self.herd.dino_three.name}!")

    def show_robo_opponent_options(self):
        self.fleet.create_fleet()
        print(f"Annnnndddd representing Team Robot we have {self.fleet.robot_one.name}, {self.fleet.robot_two.name}, and {self.fleet.robot_three.name}!")

    def display_winners(self):
        if len(self.herd.dinosaurs) == 0:
            print("Winner: Robots") 
        else:
            print("Winner: Dinosaurs")

    def coin_flip(self):
        self.competitors = ["Team Robot", "Team Dinosaur"]
        self.starting_team = random.choice(self.competitors)
        print(f"A random coin flip has determined that {self.starting_team} will have the first turn. ")
        return self.starting_team