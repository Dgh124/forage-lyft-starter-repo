from car import Car  
from part import Part, CapuletEngine, SpindlerBattery, WilloughbyEngine, SternmanEngine, NubbinBattery  

class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        
        capulet_engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)  
        spindler_battery = SpindlerBattery(last_service_date)  

        return Car(current_date, last_service_date, capulet_engine, spindler_battery)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        
        willoughby_engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)  
        spindler_battery = SpindlerBattery(last_service_date)  

       
        return Car(current_date, last_service_date, willoughby_engine, spindler_battery)

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        
        sternman_engine = SternmanEngine(last_service_date, warning_light_is_on)  
        spindler_battery = SpindlerBattery(last_service_date)  

        return Car(current_date, last_service_date, sternman_engine, spindler_battery)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        
        willoughby_engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)  
        nubbin_battery = NubbinBattery(last_service_date)  

        return Car(current_date, last_service_date, willoughby_engine, nubbin_battery)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        
        capulet_engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)  
        nubbin_battery = NubbinBattery(last_service_date)  
       
        return Car(current_date, last_service_date, capulet_engine, nubbin_battery)
