from dinosaur import Dinosaur

import random

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):  #adds the dinosaurs that the user selected to a list
        self.dinosaurs.append(self.dino_one)
        self.dinosaurs.append(self.dino_two)
        self.dinosaurs.append(self.dino_three)

    #method to let user choose which dinos to add to the herd
    def choose_dinos(self):
        #list of dinosaur attack options for the user to choose from, plus customized descriptions to print when the attacks are used
        print("\nBefore the battle begins, you have the opportunity to choose which competitors will represent Team Dinosaur. Your options are: ")
        t_rex_attacks = (("chomp", "is charging toward his opponent, he's opening his jaw wide-- Wow! Who knew that thing was so huge?-- and he's... OHHH he takes a massive bite out of ", "! OH THE HUMANITY! Or... well I guess not, am I right folks? "), ("kick", "walks right up to his opponent and BAM! He just kicked ", " clear across the stadium! His arms may be tiny, but those legs sure pack a punch!"), ("claw", "reaches up high and takes a big swipe! Holy moly, those claws are sharp! I think he just took a chunk out of ", ". That was NOT pretty."))
        pterodactyl_attacks = (("dive bomb", "shoots up into the air, looks like he is circling his prey... and his eyes lock on his target! Oh he's going for it, folks! He dives down head first, he's shooting straight toward his opponent like a missile! And he makes contact! Woah, did you folks hear that CRACK? He must have one thick skull because ", " has seen better days. That one's gonna be hard to recover from!"), ("claw", "takes off into the air immediately, he's flying in a big, low circle. Looks like he's trying to build up some speed here. OOF and just like that he pulls his claws out and swipes at ", " as he flies by! Wow, the power on this guy is unbelievable!"), ("drop attack", "leaps up and starts flying low, flies right up to his opponent and-- what is he doing?? He just picked up ", " with his claws, now he's shooting straight up into the air! He's climbing higher and higher... he must be 50 feet high... OH MY GOD! He just let go, and our robo friend is plumeting to the floor like an anvil! Genius move on the part of Team Dinosaur, that was a devastating blow!"))
        triceratops_attacks = (("stampede", "is pawing at the ground, you can see a cloud of dirt building around his feet. He starts tensing up like a runner... and he's off! Running directly at his opponent at top speed, and-- OUCH! He just ran right over ", "! If that was a human their internal organs would be scrambled! That's quite the one-man stampede! Or one-dino stampede, rather! "), ("head butt", "locks his eyes on his target, he's crouching down... this is quite the dramatic pause he's taking here, folks... and WOOSH just like that he is charging straight for ", " head first like a bull! And he makes contact! Head-on, as it were. Unbelievable! With horns like that on his head he may as well have stabbed his opponent with a pitchfork! "), ("tail whack", "is sauntering up to his opponent like he doesn't have a care in the world... seriously folks, he almost looks bored! He's lifting his tail up--boy that thing is truly massive, it looks heavy-- and... CLOCKS his opponent with it! Just clobbered 'em! Knocked ", " right over like it was nothing! Well, there's something to admire when a competitor is cocky but can back it up. That nonchalance just rubs it in! I mean just look at him folks, he's barely broken a sweat!"))
        brachiosaurus_attacks = (("sit on", "is such a peaceful fella, you do have to wonder what he really brings to the table in a battle like this. I mean the guy's a vegetarian for God's sake! Alright, he's walking up to ", " and he just... sits on it! I mean, that'll do it, folks, he is a BIG guy. So simple, yet so effective! Major points for ingenuity with this one."), ("tail whip", "is walking toward the center of the arena... this big guy looks like he'd rather be anywhere else, but he's taking one for the team. Oh he's crouching down, he's twisting... and he just SPINS himself around like a top, letting that tail of his gather up momentum and... OOH he lashes his tail right across ", " like a whip! His tail is pretty skinny compared to some of these other dinos, but he made it work to his benefit with this move! Phenomenal job!"), ("throw", "is looming large, folks! I mean holy cow, seeing him up close you really get a feel for how tall this guy is! Oh looks like he's bending down, do you think he heard me? Jeez his neck is so long, I'm surprised he can get it so close to the floor. Hmm this is interesting, he's scooping ", " up using his neck and lifting it... he's leaning back... and he LAUNCHES his opponent through the air, slams it against the wall all the way on the other side of the arena! What a feat of athleticism we all just witnessed! Amazing, I never would have thought someone could throw like that using just their neck. Although this guy's neck is longer than any arm I've ever seen, so no wonder!"))
        stegosaurus_attacks = (("body slam", "doesn't look like he has a great range of motion, I wonder what he'll do. Looks like he's crouching down... and he POUNCES, just body slammed ", "! Did anyone else hear that CRUNCH? Ouch!"), ("impale", "isn't the strongest, or the fastest, or the most agile competitor. But let's see what he comes up with. Looks like he's walking toward his opponent... he's turning his back toward ", " and pushing... I gotta say, with those spikes on his back it seems like that would hurt if he put any kind of force or speed into this attack, but it's like he's going in slow motion! What is he thinking?? He just keeps pushing back with those spikes and... oh they're getting closer to the wall, folks! They hit the wall and... OUCH he's completely impaled his opponent against the wall! What a twist!"))
        velociraptor_attacks = (("evisceration", "is running right up to his opponent, not wasting any time. He pounces on ", ", knocks it over! What's he doing now? Ooh he's tearing right into it with that big nasty-looking claw on his foot. Wow, wouldn't wanna be on the receiving end of that thing."), ("bite", "is approaching his opponent--is he yawning? Oh wait no, he's just getting ready to-- OH he takes a big old bite right out of ", "! Wow, those teeth are like knives, they're just cutting right through!"))
    
        #initializes each dinosaur with their names, attack power, and list of attacks
        dino_t_rex = Dinosaur("Tyrannosaurus Rex", 40, t_rex_attacks)
        dino_pterodactyl = Dinosaur("Pterodactyl", 20, pterodactyl_attacks)
        dino_triceratops = Dinosaur("Triceratops", 30, triceratops_attacks)
        dino_brachiosaurus = Dinosaur("Brachiosaurus", 10, brachiosaurus_attacks)
        dino_stegosaurus = Dinosaur("Stegosaurus", 20, stegosaurus_attacks)
        dino_velociraptor = Dinosaur("Velociraptor", 70, velociraptor_attacks)
        
        dino_competitors = [dino_t_rex, dino_pterodactyl, dino_triceratops, dino_brachiosaurus, dino_stegosaurus, dino_velociraptor]

        num = 1
        something = True   #irrelevant boolean used to create a while loop that has no real condition

        for item in dino_competitors:   #prompts user to select first dinosaur competitor
            print(f"{num}. {item.name}")
            num += 1
        user_choice = input("\nEnter the number of the first dinosaur you wish to add to your herd. Enter any other character for a dinosaur to be randomly assigned. ")
        if user_choice.isdigit() and int(user_choice) > 0 and int(user_choice) <= len(dino_competitors):
            dino_index = int(user_choice) - 1   #subtract 1 from the number of the dinosaur the user chose to get the index of that dinosaur
            self.dino_one = dino_competitors[dino_index]
        else:   #if the user enters a character not associated with one of the options, one is randomly selected
            self.dino_one = random.choice(dino_competitors)
            print(f"{self.dino_one.name} has been randomly selected as the first member of your herd. ")

        #prompts user to select second dinosaur competitor
        user_choice = input("\nEnter the number of the second dinosaur you wish to add to your herd. Enter any other character for a dinosaur to be randomly assigned. ")
        while something is True:    #need while loop so that selection process continues to run until option 2 is different from option 1
            if user_choice.isdigit() and int(user_choice) > 0 and int(user_choice) <= len(dino_competitors):
                dino_index = int(user_choice) - 1
                self.dino_two = dino_competitors[dino_index]
                if self.dino_two == self.dino_one:
                    user_choice = input("The dino you have selected is already in your herd. Please select a different competitor. ")
                else:
                    break   #loop breaks when option is selected that differs from previous selection
            else:
                self.dino_two = random.choice(dino_competitors)
                if self.dino_two != self.dino_one:
                    print(f"{self.dino_two.name} has been randomly selected as the second member of your herd. ")
                    break
        
        #prompts user to select third dinosaur
        user_choice = input("\nEnter the number of the third and final dinosaur you wish to add to your herd. Enter any other character for a dinosaur to be randomly assigned. ")
        while something is True:
            if user_choice.isdigit() and int(user_choice) > 0 and int(user_choice) <= len(dino_competitors):
                dino_index = int(user_choice) - 1
                self.dino_three = dino_competitors[dino_index]
                if self.dino_three == self.dino_one or self.dino_three == self.dino_two:    #makes sure selection differs from both of the previous selections
                    user_choice = input("The dinosaur you have selected is already in your herd. Please select a different competitor. ")
                else:
                    break
            else:
                self.dino_three = random.choice(dino_competitors)
                if self.dino_three != self.dino_one and self.dino_three != self.dino_two:
                    print(f"{self.dino_three.name} has been randomly selected as the last member of your herd. ")
                    break
