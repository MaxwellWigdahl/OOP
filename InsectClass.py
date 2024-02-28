import random

class Insect:
    
    def __init__(self,w,l,n):
        self.miles = w
        self.wings = l
        self.legs = 4
        self.name = n

    def calc_flight(self):
        self.miles = random.randint(1,10)

    def get_miles(self):
        return self.miles
    
    def get_name(self):
        return self.name