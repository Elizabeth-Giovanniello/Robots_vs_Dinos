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
    
    #has members of each side take turns attacking each other until one team kills off the other
    def battle(self):
        print("\nLet the battle begin! ")
        current_team = self.coin_flip()
        round = 1
        while len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) >0:   #continues to run until all members of a group have died
            nominated_bot = self.nominate_robot_champion()  #randomly chooses a member of each team for each new round
            nominated_dino = self.nominate_dino_champion()
            if current_team == "Team Robot":
                print(f"\nRound {round}: {nominated_bot.name} vs. {nominated_dino.name}")
                print(f"\nTeam Robot has nominated {nominated_bot.name} as their champion for this round. {nominated_bot.name} has decided to challenge {nominated_dino.name} to battle. ")
                print(f"\n{nominated_bot.name} and {nominated_dino.name} have entered the arena. ")
                self.robo_turn(nominated_bot, nominated_dino)
                if nominated_dino in self.herd.dinosaurs:
                    print(f"\n{nominated_dino.name} now has the chance to respond to {nominated_bot.name}'s attack. ")
                    self.dino_turn(nominated_dino, nominated_bot)
                current_team = "Team Dinosaur"    #changes current_team at the end to switch off which team attacks first
            else: 
                print(f"\nRound {round}: {nominated_dino.name} vs. {nominated_bot.name}")
                print(f"\nTeam Dinosaur has nominated {nominated_dino.name} as their champion for this round. {nominated_dino.name} has decided to challenge {nominated_bot.name} to battle. ")
                print(f"{nominated_dino.name} and {nominated_bot.name} have entered the arena. ")
                self.dino_turn(nominated_dino, nominated_bot)
                if nominated_bot in self.fleet.robots:
                    print(f"\n{nominated_bot.name} now has the chance to respond to {nominated_dino.name}'s attack. ")
                    self.robo_turn(nominated_bot, nominated_dino)
                current_team = "Team Robot"
            round += 1
            self.print_health_status(nominated_bot)
            self.print_health_status(nominated_dino)
        #ending dialogue that runs once one team has been defeated
        if len(self.herd.dinosaurs) > 0:
            print("\nAnd that does it, folks! As the only team left standing, the dinosaurs WIN! I guess that just goes to show, modern technology has its limits.")
        elif len(self.fleet.robots) > 0: 
            print("\nAnd there you have it, folks! In the ultimate showdown between robots and dinosaurs, robots are the only ones left standing. We haven't seen a defeat this crushing since the meteor hit!")

    def dino_turn(self, dino, robot):
        attacker = dino
        target = robot
        if attacker.energy_level <= 0:  #once an attacker's energy level is depleted, he needs to skip a turn to recharge it
            print(f"\nIt is now {attacker.name}'s turn to attack {target.name}, but it appears {attacker.name} is completely exhausted from previous rounds. {attacker.name} forfeits his turn so he can rest and regain his energy. ")
            attacker.power_nap()
        else:
            attacker.attack(target)
            if target.health <= 0:
                self.fleet.robots.remove(target)    #once a robot's health hits 0, it is removed from the fleet
                print(f"\nFollowing the last attack, {target.name}'s circuitry has taken too much damage, and is no longer functional. {target.name} is no longer part of this fleet.")

    def robo_turn(self, robot, dino):
        attacker = robot
        target = dino
        if attacker.power_level <= 0:   #attacker loses turn due to depleted energy
            print(f"\nIt is now {attacker.name}'s turn to attack {target.name}, but it appears {attacker.name} completely drained its battery during the previous round. {attacker.name} forfeits its turn to recharge.")
            attacker.recharge_batteries()
        else:
            attacker.attack(target)
            if target.health <= 0:     #once a dino's health hits 0, it is removed from the herd
                self.herd.dinosaurs.remove(target)
                print(f"\nFollowing the last attack, {target.name} has been too severely wounded, and has died. {target.name} is no longer part of this herd.")

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

    #determines which side gets to go first
    def coin_flip(self):
        competitors = ["Team Robot", "Team Dinosaur"]
        starting_team = random.choice(competitors)
        print(f"\nA random coin flip has determined that {starting_team} will have the first turn. ")
        return starting_team

    #chooses random competitors for each new round
    def nominate_robot_champion(self):
        nominated_bot = random.choice(self.fleet.robots)
        return nominated_bot

    def nominate_dino_champion(self):
        nominated_dino = random.choice(self.herd.dinosaurs)
        return nominated_dino

    def print_health_status(self, fighter):
        if fighter.health > 0:   #this method will only print the health status of a fighter that is still alive
            if fighter.health >= 75:
                health_status = "Excellent"
            elif fighter.health >= 50:
                health_status = "Good"
            elif    fighter.health > 10:
                health_status = "Low"
            else:
                health_status = "Critical"
            print(f"\nHealth status for {fighter.name}: {health_status}")
