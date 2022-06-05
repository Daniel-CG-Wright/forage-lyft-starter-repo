import unittest
from datetime import datetime

from battery.nubbin import nubbin
from battery.spindler import spindler
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.carrigan import Carrigan
from tire.octoprime import Octoprime

class testNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = last_service_date = today.replace(year=today.year - 5)
        batt = nubbin(last_service_date)
        self.assertTrue(batt.battery_should_be_serviced())
    
    def test_battery_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = last_service_date = today.replace(year=today.year - 2)
        batt = nubbin(last_service_date)
        self.assertFalse(batt.battery_should_be_serviced())

class testSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = last_service_date = today.replace(year=today.year - 5)
        batt = spindler(last_service_date)
        self.assertTrue(batt.battery_should_be_serviced())
    
    def test_battery_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = last_service_date = today.replace(year=today.year - 1)
        batt = spindler(last_service_date)
        self.assertFalse(batt.battery_should_be_serviced())

class testCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        currentmiles = 30001
        servicemiles = 0
        eng = CapuletEngine(currentmiles, servicemiles)
        self.assertTrue(eng.engine_should_be_serviced())
    
    def test_engine_not_need_service(self):
        currentmiles = 1
        servicemiles = 0
        eng = CapuletEngine(currentmiles, servicemiles)
        self.assertFalse(eng.engine_should_be_serviced())

class testWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        currentmiles = 60001
        servicemiles = 0
        eng = WilloughbyEngine(currentmiles, servicemiles)
        self.assertTrue(eng.engine_should_be_serviced())
    
    def test_engine_not_need_service(self):
        currentmiles = 1
        servicemiles = 0
        eng = WilloughbyEngine(currentmiles, servicemiles)
        self.assertFalse(eng.engine_should_be_serviced())

class testSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        enginelight = True
        eng = SternmanEngine(enginelight)
        self.assertTrue(eng.engine_should_be_serviced())
    
    def test_engine_not_need_service(self):
        enginelight = False
        eng = SternmanEngine(enginelight)
        self.assertFalse(eng.engine_should_be_serviced())

class testCarrigan(unittest.TestCase):
    def test_tire_needs_service(self):
        weararray = [0.95, 0.5, 0.3, 0.7]
        tire = Carrigan(weararray)
        self.assertTrue(tire.tire_needs_servicing())
    
    def test_tire_not_need_service(self):
        wear = [0.8, 0.8, 0.7, 0.1]
        tire = Carrigan(wear)
        self.assertFalse(tire.tire_needs_servicing())

class testOctoprime(unittest.TestCase):
    def test_tire_needs_service(self):
        weararray = [0.8, 0.8, 0.8, 0.8]
        tire = Octoprime(weararray)
        self.assertTrue(tire.tire_needs_servicing())
    
    def test_tire_not_need_service(self):
        wear = [0.8, 0.8, 0.7, 0.1]
        tire = Octoprime(wear)
        self.assertFalse(tire.tire_needs_servicing())
        
if __name__ == '__main__':
    unittest.main()
