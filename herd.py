from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        self.dino_one = Dinosaur("Tyrannosaurus Rex", 30)
        self.dino_two = Dinosaur("Pterodactyl", 10)
        self.dino_three = Dinosaur("Triceratops", 20)
        self.dinosaurs.append(self.dino_one, self.dino_two, self.dino_three)

    def dead_dino(self):
        for dino in self.dinosaurs:
            if dino.health <= 0:
                self.dinosaurs.remove(dino)
                print(f"Following the last attack, {dino} has been too severely wounded, and has died. {dino} is no longer part of this herd.")