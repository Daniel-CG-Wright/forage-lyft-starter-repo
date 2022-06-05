from engine.engine import engine


class CapuletEngine(engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

        self.mileage_requirement = 30000

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > self.mileage_requirement
