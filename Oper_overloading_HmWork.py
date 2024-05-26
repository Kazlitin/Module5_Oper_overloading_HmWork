class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        # Сравниваю объекты на основе атрибутов numberOfFloors и buildingType
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

# Создаю два объекта класса Building
building1 = Building(3, "Жилой дом")
building2 = Building(3, "Жилой дом")

print(building1 == building2)  # Выведет True, так как атрибуты numberOfFloors и buildingType равны

# Создаю еще один объект с другими атрибутами
building3 = Building(5, "Офисное здание")
print(building1, 'здание')
print(building1 == building3)  # Выведет False, так как атрибуты numberOfFloors или buildingType не равны