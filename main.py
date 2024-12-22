import sys  
from transport.client import Client  
from transport.vehicle import Van  
from transport.vehicle import Ship  
from transport.transportcompany import TransportCompany 

def menu():  
    print("Меню:")  
    print("1. Добавить клиента")  
    print("2. Создать фургон")  
    print("3. Создать судно")  
    print("4. Загрузить груз в транспортное средство")  
    print("5. Показать информацию о транспортном средстве")  
    print("6. Оптимизировать распределение грузов")  
    print("7. Выйти") 

def main():  
    company = TransportCompany("Компания")  

    while True:  
        menu()  
        choice = input("Выберите пункт меню: ")  

        if choice == '1':  
            name = input("Введите имя клиента: ")  
            cargo_weight = float(input("Введите вес груза клиента: ")) 
            is_vip = input("Клиент VIP? (да/нет): ").lower() == 'да'  
            client = Client(name, cargo_weight, is_vip)  
            company.add_client(client)  
            print(f"Клиент {name} добавлен.\n")  

        elif choice == '2':  
            capacity = float(input("Введите грузоподъемность фургона (в тоннах): "))  
            is_refrigerated = input("Фургон с холодильником? (да/нет): ").lower() == 'да' 
            van = Van(capacity, is_refrigerated)  
            company.add_vehicle(van)  
            print(f"Фургон создан. ID: {van.vehicle_id}\n") 

        elif choice == '3':  
            capacity = float(input("Введите грузоподъемность судна (в тоннах): "))  
            name = input("Введите название судна: ")  
            ship = Ship(capacity, name)  
            company.add_vehicle(ship)  
            print(f"Судно создано. Название: {name}, ID: {ship.vehicle_id}\n")  

        elif choice == '4':  
            client_name = input("Введите имя клиента для загрузки: ") 
            vehicle_id = input("Введите ID транспортного средства: ") 

            client = next((c for c in company.clients if c.name == client_name), None) 
            vehicle = next((v for v in company.vehicles if v.vehicle_id == vehicle_id), None)  

            if client is None:  
                print(f"Клиент с именем {client_name} не найден.\n")  
                continue

            if vehicle is None: 
                print(f"Транспортное средство с ID {vehicle_id} не найдено.\n")  
                continue

            try:
                vehicle.load_cargo(client)  
            except ValueError as e:  
                print(f"Ошибка загрузки: {e}\n")
            except TypeError as e:  
                print(f"Ошибка типа данных: {e}\n")

        elif choice == '5': 
            if not company.vehicles:  
                print("Нет доступных транспортных средств для отображения.\n")  
                continue

            for vehicle in company.vehicles: 
                print(vehicle)  
                for client in vehicle.clients_list:  
                    print(f"  - Клиент: {client.name}, Вес груза: {client.cargo_weight} т., VIP: {'Да' if client.is_vip else 'Нет'}")

            print()

        elif choice == '6':  
            company.optimize_cargo_distribution()  
            print("Распределение грузов оптимизировано.\n")

        elif choice == '7':  
            sys.exit() 

        else:  
            print("Неверный пункт меню, попробуйте снова.\n")  

if __name__ == '__main__':  
    main()  