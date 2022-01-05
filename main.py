#Using the concepts of OOP by creating classes and using objects (instances of those classes) to interact with each other, 
# create a console application that will have robots and dinosaurs fight in a battle.

#Before you begin the last user story that is highlighted in grey, write an algorithm that represents the steps of the 
# robots in the fleet and the dinosaurs in the herd battling. Think about the steps that need to happen to implement the functionality. 
# Please submit to your instructor Slack channel once completed for approval to start coding.

#User stories:

#(/5 points): As a developer, I want to make at least 7 commits with good, descriptive messages.

#(/5 points): As a developer, I want to make a class for each of the following: Robot, Dinosaur, Fleet, Herd, Weapon, Battlefield.

#(/10 points): As a developer, I want a Robot to have a name, health, and a Weapon (this needs to be its own class and object) with a name (i.e. sword) and attack power.

#(/10 points): As a developer, I want a Dinosaur to have a name, health, and attack power.

#(/10 points): As a developer, I want to instantiate three Robot objects and three Dinosaur objects and assign the appropriate values to all the objects.

#(/10 points): As a developer, I want the created Robot objects to be stored in a Fleet and the created Dinosaur objects to be stored in a Herd 
# (the Fleet and Herd must use a List to store the objects).

#(/10 points): As a developer, I want a Robot to have the ability to attack a Dinosaur and a Dinosaur to have the ability to attack a Robot on a Battlefield.

#(/10 points): As a developer, I want a Robot/Dinosaur to lose health points (loss based on attack power) when another Robot/Dinosaur successfully attacks it.

#(/10 points): As a developer, I want the battle to conclude once either all the robots in the Fleet have their health points reach zero or 
# all of the dinosaurs in the Herd have their health points reach zero.

#Bonus points:

#(/5 points): As a developer, I want a Robot to have the ability to choose from a List of different weapons that will 
# be then assigned as its own weapon.

#(/5 points): As a developer, I want a Dinosaur to have the ability to choose its attack name from a tuple of 
# different attack names before attacking a Robot in battle.

#(/2 points): As a developer, I want a Robot to have a power level and a Dinosaur to have an energy, which will 
# decrease by 10 every time they attack.




#~ Other things I may want to add in for fun: make it so user picks which two face off each round?

#~ could potentially add a "catch phrase" for each weapon choice in the list, and then add it into the print statement for the attack method. If I feel like it.

#~Rather than having the user pick the competitors we could try to make it so the same person who just got attacked retaliates on the attacker? 

#~ Also, we could make the energy drain a number associated with the attack for dinosaurs instead of attack power. Or we could mayhbe also associate attack power




from battlefield import Battlefield

todays_battle = Battlefield()

todays_battle.run_game()

# TODO add new lines to dialogue to make it more readable. change verbage of dino attacks. let user select opponents each round. consider adding specific descriptions of the attacks? 