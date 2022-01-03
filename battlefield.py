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


    def dino_turn(self):
        self.attacker = random.choice(self.herd.dinosaurs)
        self.target = random.choice(self.fleet.robots)
        print(f"This round we have {self.attacker} attacking {self.target}. ")
        self.attacker.attack(self.target)

    def robo_turn(self):
        self.attacker = random.choice(self.fleet.robots)
        self.target = random.choice(self.herd.dinosaurs)
        print(f"This round we have {self.attacker} attacking {self.target}. ")
        self.attacker.attack(self.target)


    def show_dino_opponent_options(self):
        self.herd.create_herd()
        print(f"Representing Team Dinosaur we have {self.herd.dino_one}, {self.herd.dino_two}, and {self.herd.dino_three}!")

    def show_robo_opponent_options(self):
        self.fleet.create_fleet()
        print(f"Annnnndddd representing Team Robot we have {self.fleet.robot_one}, {self.fleet.robot_two}, and {self.fleet.robot_three}!")

    def display_winners(self):
        if len(herd.dinosaurs) == 0:
            print("Winner: Robots") #COME BACK TO THIS

    def coin_flip(self):
        self.competitors = ["Team Robot", "Team Dinosaur"]
        self.starting_team = random.choice(self.competitors)
        print(f"A random coin flip has determined that {self.starting_team} will have the first turn. ")
        return self.starting_team