from abc import ABC, abstractmethod


class Battery(ABC):

    def __init__(self):
        pass
        
        
    @abstractmethod
    def battery_should_be_serviced(self):
        pass


