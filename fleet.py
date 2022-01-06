from robot import Robot

import random

class Fleet:
    def __init__(self):
        self.robots = []
    
    def create_fleet(self):    #adds selected robots to a list
        self.robots.append(self.robot_one)
        self.robots.append(self.robot_two)
        self.robots.append(self.robot_three)

    #method to let user choose which robots to include in the fleet
    def choose_robots(self):
        print("\nNow it's time to choose which competitors will represent Team Robot. Your options are: ")
        #list of weapons options for each robot, plus their associated attack power
        roomba_weapons = [["shards of glass from a lamp you broke", 5], ["thumb tacks that fell on the floor", 3], ["a dust bomb", 10]]
        alexa_weapons = [["a piercingly high-pitched noise that shuts down one's central nervous system", 50], ["mind control", 10]] 
        blender_weapons = [["rotating blades", 20], ["an exploding kale smoothie", 10], ["ice cube projectiles", 25]]
        drone_weapons = [["a chemical bomb", 35], ["a cluster bomb", 40], ["a hand grenade", 20], ["a machine gun", 25], ["a nuclear missile", 90], ["a glitter bomb", 5]] 
        r2d2_weapons = [["the Force", 15], ["a lightsaber", 25], ["space laser gun", 20]]
        microwave_weapons = [["a high concentration of electromagnetic waves", 15], ["an irritating beep that won't stop even when its door is opened", 1], ["the sharp corner of its swinging door", 5]]
        wall_e_weapons = [["a twinkie", 1], ["crushed garbage", 10], ["a trash compactor", 20]]

        #initializing each robot with name and list of weapons
        robot_roomba = Robot("Roomba", roomba_weapons)
        robot_alexa = Robot("Alexa", alexa_weapons)
        robot_blender = Robot("Fruit Ninja Blender", blender_weapons)
        robot_drone = Robot("Military-grade Drone", drone_weapons)
        robot_r2d2 = Robot("R2D2", r2d2_weapons)
        robot_microwave = Robot("Microwave oven", microwave_weapons)
        robot_wall_e = Robot("WALL-E", wall_e_weapons)

        robot_competitors = [robot_roomba, robot_alexa, robot_blender, robot_drone, robot_r2d2, robot_microwave, robot_wall_e]

        num = 1
        something = True

        for item in robot_competitors:  #loop to print each item in a numbered list
            print(f"{num}. {item.name}")
            num += 1
        user_choice = input("\nEnter the number of the first robot you wish to add to your fleet. Enter any other character for a robot to be randomly assigned. ")
        if user_choice.isdigit() and int(user_choice) > 0 and int(user_choice) <= len(robot_competitors):
            robot_index = int(user_choice) - 1
            self.robot_one = robot_competitors[robot_index]
        else:   #if user enters invalid character, robot is randomly selected
            self.robot_one = random.choice(robot_competitors)
            print(f"{self.robot_one.name} has been randomly selected as the first member of your fleet. ")
        
        self.robot_one.choose_weapon()  #after each robot is chosen, the user is prompted to choose their weapon

        user_choice = input("\nEnter the number of the second robot you wish to add to your fleet. Enter any other character for a robot to be randomly assigned. ")
        while something is True:    #while loop so that the same robot can't be selected twice
            if user_choice.isdigit() and int(user_choice) > 0 and int(user_choice) <= len(robot_competitors):
                robot_index = int(user_choice) - 1
                self.robot_two = robot_competitors[robot_index]
                if self.robot_two == self.robot_one:
                    user_choice = input("The robot you have selected is already in your fleet. Please select a different competitor. ")
                else:
                    break
            else:
                self.robot_two = random.choice(robot_competitors)
                if self.robot_two != self.robot_one:
                    print(f"{self.robot_two.name} has been randomly selected as the second member of your fleet. ")
                    break

        self.robot_two.choose_weapon()

        user_choice = input("\nEnter the number of the third and final robot you wish to add to your fleet. Enter any other character for a robot to be randomly assigned. ")
        while something is True:
            if user_choice.isdigit() and int(user_choice) > 0 and int(user_choice) <= len(robot_competitors):
                robot_index = int(user_choice) - 1
                self.robot_three = robot_competitors[robot_index]
                if self.robot_three == self.robot_one or self.robot_three == self.robot_two:
                    user_choice = input("The robot you have selected is already in your fleet. Please select a different competitor. ")
                else:
                    break
            else:
                self.robot_three = random.choice(robot_competitors)
                if self.robot_three != self.robot_one and self.robot_three != self.robot_two:
                    print(f"{self.robot_three.name} has been randomly selected as the last member of your fleet. ")
                    break
        
        self.robot_three.choose_weapon()