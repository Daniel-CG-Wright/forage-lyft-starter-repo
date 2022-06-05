from abc import ABC, abstractmethod

class Tire(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def tire_needs_servicing(self):
        pass
    