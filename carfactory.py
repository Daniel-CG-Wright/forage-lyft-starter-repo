from cProfile import label
from re import L
from car import Car

from battery.battery import battery

from battery.nubbin import nubbin
from battery.spindler import spindler

from engine.engine import engine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class CarFactory:

    def __init__(self):
        pass

    def create_calliope(self, last_service_date, current_mileage, last_service_mileage):

        batt = spindler(last_service_date)
        eng = CapuletEngine(current_mileage, last_service_mileage)

        return Car(batt, eng)
    
    def create_glissade(self, last_service_date, current_mileage, last_service_mileage):

        batt = spindler(last_service_date)
        eng = WilloughbyEngine(current_mileage, last_service_mileage)

        return Car(batt, eng)

    def create_palindrome(self, last_service_date, engine_light_on):

        batt = spindler(last_service_date)
        eng = SternmanEngine(engine_light_on)

        return Car(batt, eng)
    
    def create_rorschach(self, last_service_date, current_mileage, last_service_mileage):

        batt = nubbin(last_service_date)
        eng = WilloughbyEngine(current_mileage, last_service_mileage)

        return Car(batt, eng)
    
    def create_thovex(self, last_service_date, current_mileage, last_service_mileage):

        batt = nubbin(last_service_date)
        eng = CapuletEngine(current_mileage, last_service_mileage)

        return Car(batt, eng)
    
    