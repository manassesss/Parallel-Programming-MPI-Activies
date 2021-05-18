import numpy

class Calc_PI():

    def __init__(self, n):
        self.ene = n
    

    def sum(self):
        if self.ene == 0:
            return 0
        for i in range(self.ene):
            summed = 1/(1+((i-0.5)/self.ene)^2)
    
    def calc_PI(self):
        if self.ene == 0:
            return 0
        pi = ((1/self.ene)* self.sum())*4
        return pi
