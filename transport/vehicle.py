import uuid
from transport.client import Client
class Vehicle:
    def __init__(self, capacity):
        self.vehicle_id = str(uuid.uuid4())
        self.capacity = self.validate_capacity(capacity)
        self.current_load = 0
        self.clients_list = []
    def validate_capacity(self, capacity): 
        if not isinstance(capacity, (int, float)) or capacity <= 0:
            raise ValueError("Грузоподъемность - положительное число ")
        return capacity 

    def load_cargo(self, client):
        if self.current_load + client.cargo_weight <= self.capacity:
            self.current_load += client.cargo_weight
            self.clients_list.append(client)
            return True
        return False

    def __str__(self):
        return f"ID транспорта:{self.vehicle_id},грузоподъёмность:{self.capacity},текущая загрузка:{self.current_load}"
class Van(Vehicle):
    def __init__(self, capacity, is_refrigerated=False):  
        super().__init__(capacity) 
        self.is_refrigerated = is_refrigerated  
class Ship (Vehicle):
     def __init__(self, capacity, name): 
        super().__init__(capacity)  
        self.name = name  