class Fleet:
    def __init__(self):
        self.robots = []
    
    def create_fleet(self):
        pass

    def dead_robot(self):
        for robot in self.robots:
            if robot.health <= 0:
                self.robots.remove(robot)
                print(f"Following the last attack, {robot}'s circuitry has taken too much damage, and is no longer functional. {robot} is no longer part of this fleet.")
                