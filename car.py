from service import Serviceable

class Car(Serviceable):
    def __init__(self, battery, engine, tires):
        self.battery = battery
        self.engine = engine
        self.tires = tires
    
    def needs_service(self):
        if self.engine.engine_should_be_serviced() or self.battery.battery_should_be_serviced() or self.tires.tire_needs_servicing():
            return True
        
        else: return False


