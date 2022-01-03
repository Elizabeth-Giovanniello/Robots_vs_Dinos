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
        self.coin_flip()
        self.battle()

    def display_welcome(self):
        print("Welcome to the ultimate battle of the ages, where we pit the ingenuity of modern technology against the brute strength of the prehistoric era! In this no holds barred fight to the death, I give you: Robots versus Dinosaurs!")
    
    def battle(self):
        pass

    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

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
        competitors = ["Team Robot", "Team Dinosaur"]
        starting_team = random.choice(competitors)
        print(f"A random coin flip has determined that {starting_team} will have the first turn. ")
        if starting_team == "Team Robot":
            self.robo_turn()