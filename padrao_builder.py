class Vehicle:
    def __init__(self, model, engine, color):
        self.model = model
        self.engine = engine
        self.color = color
        self.accessories = []

    def add_accessory(self, accessory):
        self.accessories.append(accessory)

    def __str__(self):
        return f"Vehicle {self.model} - Engine: {self.engine} - Color: {self.color} - Accessories: {', '.join(self.accessories)}"


class VehicleBuilder:
    def __init__(self, model, engine, color):
        self.vehicle = Vehicle(model, engine, color)

    def add_accessory(self, accessory):
        self.vehicle.add_accessory(accessory)
        return self

    def get_vehicle(self):
        return self.vehicle


class Director:
    def build_luxury_car(self, builder):
        return builder.add_accessory("Ar condicionado").add_accessory("Bancos de couro")

    def build_sport_motorcycle(self, builder):
        return builder.add_accessory("Escape esportivo").add_accessory("Assento monoposto")

    def build_robust_truck(self, builder):
        return builder.add_accessory("Carroceria reforçada").add_accessory("Cabine espaçosa")


diretor = Director()

builder_carro = VehicleBuilder("Sedan", "Motor V6", "Preto")
carro_luxo = diretor.build_luxury_car(builder_carro)
veiculo_carro_luxo = builder_carro.get_vehicle()
print(veiculo_carro_luxo)

builder_moto = VehicleBuilder("Esportiva", "Motor 1000cc", "Vermelho")
