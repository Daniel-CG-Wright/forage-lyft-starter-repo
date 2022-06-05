from tire.tire import Tire

class Carrigan(Tire):

    def __init__(self, weararray):
        self.weararray = weararray

    def tire_needs_servicing(self):
        needservice = False
        for i in self.weararray:
            if i >= 0.9: needservice = True
        
        return needservice
        