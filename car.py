from service import Serviceable

class Car(Serviceable):
    def __init__(self, battery, engine):
        self.battery = battery
        self.engine = engine

    
    def needs_service(self):
        if self.engine.engine_should_be_serviced() or self.battery.battery_should_be_serviced():
            return True
        
        else: return False


