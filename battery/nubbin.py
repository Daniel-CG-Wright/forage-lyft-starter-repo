from battery import battery
from datetime import datetime

class nubbin(battery):

    def __init__(self, last_service_date):

        self.today = datetime.today().date()

        self.service_date = last_service_date

        self.service_years = 4

    def battery_should_be_serviced(self):
        
        threshold_date = self.service_date.replace(year=self.service_date.year + self.service_years)
        if threshold_date < self.today:
            return True
        else:
            return False
    