from abc import ABC, abstractmethod
from datetime import datetime


class Part():
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        
    @abstractmethod
    def service_required(self):
        pass
    
    
# class Engine(self, Part, ABC):
#     def __init__(self, last_service_date):
#         self.last_service_date = last_service_date
#     @abstractmethod
#     def needs_service(self):
#         pass
    
    
    
class CapuletEngine(Part, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000
    
    
    
class SternmanEngine(Part, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
        
        
        
class WilloughbyEngine(Part, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000


    
class SpindlerBattery(Part, ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        
        def needs_service(self):
            if self.service_threshold_date < datetime.today().date():
                return True
            else:
                return False
            
            
            
class NubbinBattery(Part, ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        
        def needs_service(self):
            if self.service_threshold_date < datetime.today().date():
                return True
            else:
                return False