class Client():
    def __init__(self, name,cargo_weight,is_vip=False):
        self.name = name
        self.cargo_weight = cargo_weight
        self.is_vip = is_vip
    def validate_cargo_weight(self, cargo_weight):  
        if not isinstance(cargo_weight, (int, float)) or cargo_weight <= 0:  
            raise ValueError("Вес груза должен быть положительным числом")
        return cargo_weight  