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
        t_rex_attacks = (("chomp", "He's charging toward his opponent, he's opening his jaw wide-- Wow! Who knew that thing was so huge?-- and he's... OHHH he takes a massive bite out of ", "! OH THE HUMANITY! Or... well I guess not, am I right folks? "), ("kick", "He walks right up to his opponent and BAM! He just kicked ", " clear across the stadium! His arms may be tiny, but those legs sure pack a punch!"), ("claw", "He reaches up high and takes a big swipe! Holy moly, those claws are sharp! I think he just took a chunk out of ", ". That was NOT pretty."))
        pterodactyl_attacks = (("dive bomb", "He shoots up into the air, looks like he is circling his prey... and his eyes lock on his target! Oh he's going for it, folks! He dives down head first, he's shooting straight toward his opponent like a missile! And he makes contact! Woah, did you folks hear that CRACK? He must have one thick skull because ", " has seen better days. That one's gonna be hard to recover from!"), ("claw", "He takes off into the air immediately, he's flying in a big, low circle. Looks like he's trying to build up some speed here. OOF and just like that he pulls his claws out and swipes at ", " as he flies by! Wow, the power on this guy is unbelievable!"), ("drop attack", "He leaps up and starts flying low, flies right up to his opponent and-- what is he doing?? He just picked up ", " with his claws, now he's shooting straight up into the air! He's climbing higher and higher... he must be 50 feet high... OH MY GOD! He just let go, and our robo friend is plumeting to the floor like an anvil! Genius move on the part of Team Dinosaur, that was a devastating blow!"))
        triceratops_attacks = (("stampede", "He's pawing at the ground, you can see a cloud of dirt building around his feet. He starts tensing up like a runner... and he's off! Running directly at his opponent at top speed, and-- OUCH! He just ran right over ", "! If that was a human their internal organs would be scrambled! That's quite the one-man stampede! Or one-dino stampede, rather. "), ("head butt", "He locks his eyes on his target, he's crouching down... this is quite the dramatic pause he's taking here, folks... and WOOSH just like that he is charging straight for ", " head first like a bull! And he makes contact! Head-on, as it were. Unbelievable! With horns like that on his head he may as well have stabbed his opponent with a pitchfork! "), ("tail whack", "He's sauntering up to his opponent like he doesn't have a care in the world... seriously folks, he almost looks bored! He's lifting his tail up--boy that thing is truly massive, it looks heavy-- and... CLOCKS his opponent with it! Just clobbered 'em! Knocked ", " right over like it was nothing! Well, there's something to admire when a competitor is cocky but can back it up. That nonchalance just rubs it in! I mean just look at him folks, he's barely broken a sweat!"))
        brachiosaurus_attacks = (("sit on", "He's such a peaceful fella, you do have to wonder what he really brings to the table in a battle like this. I mean the guy's a vegetarian for God's sake! Alright, he's walking up to ", " and he just... sits on it! I mean, that'll do it, folks, he is a BIG guy. So simple, yet so effective! Major points for ingenuity with this one."), ("tail whip", "He's walking toward the center... this big guy looks like he'd rather be anywhere else, but he's taking one for the team. Oh he's crouching down, he's twisting... and he just SPINS himself around like a top, letting that tail of his gather up momentum and... OOH he lashes his tail right across ", " like a whip! His tail is pretty skinny compared to some of these other dinos, but he made it work to his benefit with this move! Phenomenal job!"), ("throw", "Wow, seeing him up close you really get a feel for how tall this guy is! Oh looks like he's bending down, do you think he heard me? "))
        stegosaurus_attacks = ("body slamming", "impaling on back spikes")
        velociraptor_attacks = ("eviscerating with claws" "tearing flesh with teeth")
        # TODO come back and make the ^above attacks make more sense with the grammar of the print statements

        dino_t_rex = Dinosaur("Tyrannosaurus Rex", 40, t_rex_attacks)
        dino_pterodactyl = Dinosaur("Pterodactyl", 20, pterodactyl_attacks)
        dino_triceratops = Dinosaur("Triceratops", 30, triceratops_attacks)
        dino_brachiosaurus = Dinosaur("Brachiosaurus", 10, brachiosaurus_attacks)
        dino_stegosaurus = Dinosaur("Stegosaurus", 20, stegosaurus_attacks)
        dino_velociraptor = Dinosaur("Velociraptor", 70, velociraptor_attacks)
        
        dino_competitors = [dino_t_rex, dino_pterodactyl, dino_triceratops, dino_brachiosaurus, dino_stegosaurus]

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
