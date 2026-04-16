class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
        
    def work(self, hours):
        self.battery -= hours * 10
        if self.battery < 0:
            self.battery = 0
        print(f"{self.name} worked for {hours} hours. Battery level: {self.battery}%")
    
    def charge(self, hours):
        self.battery += hours * 20
        if self.battery > 100:
            self.battery = 100
        print(f"{self.name} charged for {hours} hours. Battery level: {self.battery}%")

    def show_battery(self):
        return f"{self.name} has {self.battery}% battery left."

    def introduce(self):
        return f"Hello, I am {self.name} and I have a {self.battery}% battery level."
robot1 = Robot("Robo", 50)
robot1.introduce()
robot1.work(3)
robot1.charge(2)
print(robot1.show_battery())
