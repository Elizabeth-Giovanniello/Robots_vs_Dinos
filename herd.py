from dinosaur import Dinosaur

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
