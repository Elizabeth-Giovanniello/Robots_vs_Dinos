class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        pass

    def dead_dino(self):
        for dino in self.dinosaurs:
            if dino.health <= 0:
                self.dinosaurs.remove(dino)
                print(f"Following the last attack, {dino} has been too severely wounded, and has died. {dino} is no longer part of this herd.")