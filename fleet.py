from robot import Robot

import random

class Fleet:
    def __init__(self):
        self.robots = []
    
    def create_fleet(self):
        self.robot_one = Robot("Roomba", "shards of glass from a lamp you broke", 5)
        self.robot_two = Robot("Alexa", "a piercingly high-pitched noise that shuts down one's central nervous system", 50)
        self.robot_three = Robot("Fruit Ninja blender", "rotating blades", 20)
        self.robots.append(self.robot_one)
        self.robots.append(self.robot_two)
        self.robots.append(self.robot_three)


    def choose_robots(self):
        print("Before the battle begins, YOU have the opportunity to choose which competitors will represent Team Robot. Your options are: ")
        self.roomba_weapons = [["shards of glass from a lamp you broke", 5], ["thumb tacks that fell on the floor", 3], ["dust bomb", 10]]
        self.alexa_weapons = [["a piercingly high-pitched noise that shuts down one's central nervous system", 50], []]
        self.blender_weapons = [["rotating blades", 20], ["an exploding kale smoothie", 10], ["ice cube projectiles", 25]]
        self.drone_weapons = [["a chemical bomb", 35], ["a cluster bomb", 40], ["a hand grenade", 20], ["a machine gun", 25], ["a nuclear missile", 90]] 
        self.r2d2_weapons = [["the Force", 15], ["a lightsaber", 25], ["space laser gun", 20]]
        self.microwave_weapons = [["a high concentration of electromagnetic waves", 15], ["an irritating beep that won't stop even when its door is opened", 1], ["the sharp corner of its swining door", 5]]

        self.robot_roomba = Robot("Roomba", self.roomba_weapons)
        self.robot_alexa = Robot("Alexa", self.alexa_weapons)
        self.robot_blender = Robot("Fruit Ninja Blender", self.blender_weapons)
        self.robot_drone = Robot("Military-grade Drone", self.drone_weapons)
        self.robot_r2d2 = Robot("R2D2", self.r2d2_weapons)
        self.robot_microwave = Robot("Microwave oven", self.microwave_weapons)

        self.robot_competitors = [self.robot_roomba, self.robot_alexa, self.robot_blender, self.robot_drone, self.robot_r2d2, self.robot_microwave]

        self.num = 1

        for item in self.robot_competitors:
            print(f"{self.num}. {item.name}")
            self.num += 1
        self.user_choice = input("Enter the number of the first robot you wish to add to your fleet. Enter any other character for a robot to be randomly assigned. ")
        if int(self.user_choice) > 0 and int(self.user_choice) <= len(self.robot_competitors):
            self.robot_index = int(self.user_choice) - 1
            self.robot_one = self.robot_competitors[self.robot_index]
        else:
            self.robot_one = random.choice(self.robot_competitors)
            print(f"{self.robot_one.name} has been randomly selected as the first member of your fleet. ")
        
        self.user_choice = input("Enter the number of the second robot you wish to add to your fleet. Enter any other character for a robot to be randomly assigned. ")
        if int(self.user_choice) > 0 and int(self.user_choice) <= len(self.robot_competitors):
            self.robot_index = int(self.user_choice) - 1
            self.robot_two = self.robot_competitors[self.robot_index]
        else:
            self.robot_one = random.choice(self.robot_competitors)
            print(f"{self.robot_one.name} has been randomly selected as the second member of your fleet. ")

            input("The robot you have selected is already in your fleet. Please select a different competitor. ")