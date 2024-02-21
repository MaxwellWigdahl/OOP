import random

class Insect:
    
    def __init__(self):
        self.miles = 0
        self.wings = 2
        self.legs = 4

    def flight(self):
        self.miles = random.randint(1,11)

    def get_miles(self):
        return self.miles