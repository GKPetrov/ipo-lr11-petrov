from transport.vehicle import Vehicle
from transport.client import Client
class TransportCompany():
    def __init__(self, name):
        self.name = name
        self.vehicles = []
        self.clients = []

    def add_vehicle(self, vehicle):  
        if not isinstance(vehicle, Vehicle):  
            raise TypeError("Ожидается объект класса Vehicle")
        self.vehicles.append(vehicle) 

    def list_vehicles(self):
        return [str(vehicle) for vehicle in self.vehicles]

    def add_client(self, client):
        if not isinstance(client, Client):  
            raise TypeError("Ожидается объект класса Client")
        self.clients.append(client)  

    def optimize_cargo_distribution(self):
        self.clients.sort(key=lambda x: (-x.is_vip, x.cargo_weight))  
        for client in self.clients:  
            for vehicle in self.vehicles: 
                if vehicle.current_load + client.cargo_weight <= vehicle.capacity:  
                    vehicle.load_cargo(client)  
                    break  