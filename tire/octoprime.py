from tire.tire import Tire

class Octoprime(Tire):
    def __init__(self, weararray):
        self.weararray = weararray

    def tire_needs_servicing(self):
        sumtires = 0
        for i in self.weararray:
            sumtires += i
        
        return sumtires >= 3

