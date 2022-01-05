from fleet import Fleet
from herd import Herd

import random

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
    
    def run_game(self):
        self.display_welcome()
        self.herd.choose_dinos()
        self.fleet.choose_robots()
        self.show_dino_opponent_options()
        self.show_robo_opponent_options()
        self.battle()
        self.display_winners()

    def display_welcome(self):
        print("\nWelcome to the ultimate battle of the ages, where we pit the ingenuity of modern technology against the brute strength of the prehistoric era! In this no holds barred fight to the death, I give you: Robots versus Dinosaurs!")
    
    def battle(self):
        print("Let the battle begin! ")
        current_team = self.coin_flip()
        while len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) >0:
            if current_team == "Team Robot":
                self.robo_turn()
                current_team = "Team Dinosaur"
            else: 
                self.dino_turn()
                current_team = "Team Robot"
        if len(self.herd.dinosaurs) > 0:
            print("\nAnd that does it, folks! As the only team left standing, the dinosaurs WIN! I guess that just goes to show, modern technology has its limits.")
        elif len(self.fleet.robots) > 0: 
            print("\nAnd there you have it, folks! In the ultimate showdown between robots and dinosaurs, robots are the only ones left standing. We haven't seen a defeat this crushing since the meteor hit!")

    def dino_turn(self):
        attacker = random.choice(self.herd.dinosaurs)
        target = random.choice(self.fleet.robots)
        if attacker.energy_level <= 0:  #once an attacker's energy level is depleted, he needs to skip a turn to recharge it
            print(f"\nThis round we have {attacker.name} attacking {target.name}, but it appears {attacker.name} is completely exhausted from previous rounds. {attacker.name} forfeits his turn so he can rest and regain his energy. ")
            attacker.power_nap()
        else:
            print(f"\nThis round we have {attacker.name} attacking {target.name}. ")
            attacker.attack(target)
            if target.health <= 0:
                self.fleet.robots.remove(target)
                print(f"Following the last attack, {target.name}'s circuitry has taken too much damage, and is no longer functional. {target.name} is no longer part of this fleet.")

    def robo_turn(self):
        attacker = random.choice(self.fleet.robots)
        target = random.choice(self.herd.dinosaurs)
        if attacker.power_level <= 0:
            print(f"\nThis round we have {attacker.name} attacking {target.name}, but it appears {attacker.name} completely drained its battery during the previous round. {attacker.name} forfeits its turn to recharge.")
            attacker.recharge_batteries()
        else:
            print(f"\nThis round we have {attacker.name} attacking {target.name}. ")
            attacker.attack(target)
            if target.health <= 0:
                self.herd.dinosaurs.remove(target)
                print(f"Following the last attack, {target.name} has been too severely wounded, and has died. {target.name} is no longer part of this herd.")

    def show_dino_opponent_options(self):
        self.herd.create_herd()
        print(f"\nRepresenting Team Dinosaur we have {self.herd.dino_one.name}, {self.herd.dino_two.name}, and {self.herd.dino_three.name}!")

    def show_robo_opponent_options(self):
        self.fleet.create_fleet()
        print(f"Annnnndddd representing Team Robot we have {self.fleet.robot_one.name}, {self.fleet.robot_two.name}, and {self.fleet.robot_three.name}!")

    def display_winners(self):
        if len(self.herd.dinosaurs) == 0:
            print("Winner: Robots") 
        else:
            print("Winner: Dinosaurs")

    def coin_flip(self):
        competitors = ["Team Robot", "Team Dinosaur"]
        starting_team = random.choice(competitors)
        print(f"\nA random coin flip has determined that {starting_team} will have the first turn. ")
        return starting_team
