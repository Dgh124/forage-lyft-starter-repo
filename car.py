from abc import ABC, abstractmethod

class Car():
    def __init__(self, current_date, last_service_date, engine, battery):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.parts = [engine, battery]
        
    def needs_service(self):
        for part in self.parts:
            if part.needs_service() == True:
                return True
        return False
        
    def add_part(self, Part):
        self.list.append(Part)
    
    def remove_part(self, Part):
        if Part in self.parts:
            self.parts.remove(Part)
        
        

