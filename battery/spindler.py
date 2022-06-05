from battery.battery import Battery
from datetime import datetime

class spindler(Battery):
    def __init__(self, last_service_date):
        self.today = datetime.today().date()

        self.service_date = last_service_date
        self.service_years = 2
    

    def battery_should_be_serviced(self):
        
        threshold_date = self.service_date.replace(year=self.service_date.year + self.service_years)
        if threshold_date < self.today:
            return True
        else:
            return False
    