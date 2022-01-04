from dinosaur import Dinosaur

import random

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        self.dino_one = Dinosaur("Tyrannosaurus Rex", 30)
        self.dino_two = Dinosaur("Pterodactyl", 10)
        self.dino_three = Dinosaur("Triceratops", 20)
        self.dinosaurs.append(self.dino_one)
        self.dinosaurs.append(self.dino_two)
        self.dinosaurs.append(self.dino_three)



    def choose_dinos(self):
        print("Before the battle begins, YOU have the opportunity to choose which competitors will represent Team Dinosaur. Your options are: ")
        self.t_rex_attacks = ("chomping down on", "kicking", "clawing at")
        self.pterodactyl_attacks = ("dive bombing", "clawing at", "picking it up, flying up 50 feet, and letting go")
        self.triceratops_attacks = ("stampede", "head-butting it with horns", "clocking it with tail")
        self.brachiosaurus_attacks = ("sit on", "swipe with tail", "throw")

        # TODO come back and make the ^above attacks make more sense with the grammar of the print statements

        self.dino_t_rex = Dinosaur("Tyrannosaurus Rex", 40, self.t_rex_attacks)
        self.dino_pterodactyl = Dinosaur("Pterodactyl", 20, self.pterodactyl_attacks)
        self.dino_triceratops = Dinosaur("Triceratops", 30, self.triceratops_attacks)
        self.dino_brachiosaurus = Dinosaur("Brachiosaurus", 10, self.brachiosaurus_attacks)
        

        self.dino_competitors = [self.dino_t_rex, self.dino_pterodactyl, self.dino_triceratops, self.dino_brachiosaurus]

        self.num = 1
        self.something = True

        for item in self.dino_competitors:
            print(f"{self.num}. {item.name}")
            self.num += 1
        self.user_choice = input("Enter the number of the first dinosaur you wish to add to your herd. Enter any other character for a dinosaur to be randomly assigned. ")
        if self.user_choice.isdigit() and int(self.user_choice) > 0 and int(self.user_choice) <= len(self.dino_competitors):
            self.dino_index = int(self.user_choice) - 1
            self.dino_one = self.dino_competitors[self.dino_index]
        else:
            self.dino_one = random.choice(self.dino_competitors)
            print(f"{self.dino_one.name} has been randomly selected as the first member of your herd. ")

        self.user_choice = input("Enter the number of the second dinosaur you wish to add to your herd. Enter any other character for a dinosaur to be randomly assigned. ")
        while self.something is True:
            if self.user_choice.isdigit() and int(self.user_choice) > 0 and int(self.user_choice) <= len(self.dino_competitors):
                self.dino_index = int(self.user_choice) - 1
                self.dino_two = self.dino_competitors[self.dino_index]
                if self.dino_two == self.dino_one:
                    self.user_choice = input("The dino you have selected is already in your herd. Please select a different competitor. ")
                else:
                    break
            else:
                self.dino_two = random.choice(self.dino_competitors)
                if self.dino_two != self.dino_one:
                    print(f"{self.dino_two.name} has been randomly selected as the second member of your herd. ")
                    break

        self.user_choice = input("Enter the number of the third and final dinosaur you wish to add to your herd. Enter any other character for a dinosaur to be randomly assigned. ")
        while self.something is True:
            if self.user_choice.isdigit() and int(self.user_choice) > 0 and int(self.user_choice) <= len(self.dino_competitors):
                self.dino_index = int(self.user_choice) - 1
                self.dino_three = self.dino_competitors[self.dino_index]
                if self.dino_three == self.dino_one or self.dino_three == self.dino_two:
                    self.user_choice = input("The dinosaur you have selected is already in your herd. Please select a different competitor. ")
                else:
                    break
            else:
                self.dino_three = random.choice(self.dino_competitors)
                if self.dino_three != self.dino_one and self.dino_three != self.dino_two:
                    print(f"{self.dino_three.name} has been randomly selected as the last member of your herd. ")
                    break
