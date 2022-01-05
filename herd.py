from dinosaur import Dinosaur

import random

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        self.dinosaurs.append(self.dino_one)
        self.dinosaurs.append(self.dino_two)
        self.dinosaurs.append(self.dino_three)

    def choose_dinos(self):
        print("\nBefore the battle begins, you have the opportunity to choose which competitors will represent Team Dinosaur. Your options are: ")
        t_rex_attacks = ("chomping down on", "kicking", "clawing at")
        pterodactyl_attacks = ("dive bombing", "clawing at", "picking it up, flying up 50 feet, and letting go")
        triceratops_attacks = ("stampede", "head-butting it with horns", "clocking it with tail")
        brachiosaurus_attacks = ("sit on", "swipe with tail", "throw")

        # TODO come back and make the ^above attacks make more sense with the grammar of the print statements

        dino_t_rex = Dinosaur("Tyrannosaurus Rex", 40, t_rex_attacks)
        dino_pterodactyl = Dinosaur("Pterodactyl", 20, pterodactyl_attacks)
        dino_triceratops = Dinosaur("Triceratops", 30, triceratops_attacks)
        dino_brachiosaurus = Dinosaur("Brachiosaurus", 10, brachiosaurus_attacks)
        

        dino_competitors = [dino_t_rex, dino_pterodactyl, dino_triceratops, dino_brachiosaurus]

        num = 1
        something = True

        for item in dino_competitors:
            print(f"{num}. {item.name}")
            num += 1
        user_choice = input("\nEnter the number of the first dinosaur you wish to add to your herd. Enter any other character for a dinosaur to be randomly assigned. ")
        if user_choice.isdigit() and int(user_choice) > 0 and int(user_choice) <= len(dino_competitors):
            dino_index = int(user_choice) - 1
            self.dino_one = dino_competitors[dino_index]
        else:
            self.dino_one = random.choice(dino_competitors)
            print(f"{self.dino_one.name} has been randomly selected as the first member of your herd. ")

        user_choice = input("\nEnter the number of the second dinosaur you wish to add to your herd. Enter any other character for a dinosaur to be randomly assigned. ")
        while something is True:
            if user_choice.isdigit() and int(user_choice) > 0 and int(user_choice) <= len(dino_competitors):
                dino_index = int(user_choice) - 1
                self.dino_two = dino_competitors[dino_index]
                if self.dino_two == self.dino_one:
                    user_choice = input("The dino you have selected is already in your herd. Please select a different competitor. ")
                else:
                    break
            else:
                self.dino_two = random.choice(dino_competitors)
                if self.dino_two != self.dino_one:
                    print(f"{self.dino_two.name} has been randomly selected as the second member of your herd. ")
                    break

        user_choice = input("\nEnter the number of the third and final dinosaur you wish to add to your herd. Enter any other character for a dinosaur to be randomly assigned. ")
        while something is True:
            if user_choice.isdigit() and int(user_choice) > 0 and int(user_choice) <= len(dino_competitors):
                dino_index = int(user_choice) - 1
                self.dino_three = dino_competitors[dino_index]
                if self.dino_three == self.dino_one or self.dino_three == self.dino_two:
                    user_choice = input("The dinosaur you have selected is already in your herd. Please select a different competitor. ")
                else:
                    break
            else:
                self.dino_three = random.choice(dino_competitors)
                if self.dino_three != self.dino_one and self.dino_three != self.dino_two:
                    print(f"{self.dino_three.name} has been randomly selected as the last member of your herd. ")
                    break
