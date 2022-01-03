from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
    
    def create_fleet(self):
        self.robot_one = Robot("Rumba", "shards of glass from a lamp you broke", 5)
        self.robot_two = Robot("Alexa", "emission of a piercingly high-pitched noise that shuts down your central nervous system", 50)
        self.robot_three = Robot("Fruit ninja blender", "rotating blades", 20)
        self.robots.append(self.robot_one, self.robot_two, self.robot_three)

    def dead_robot(self):
        for robot in self.robots:
            if robot.health <= 0:
                self.robots.remove(robot)
                print(f"Following the last attack, {robot}'s circuitry has taken too much damage, and is no longer functional. {robot} is no longer part of this fleet.")
