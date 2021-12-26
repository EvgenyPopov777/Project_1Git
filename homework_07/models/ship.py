from .vehiclebase import VehicleBase
class Ship(VehicleBase):
    def __init__(self):
        print('Пример вызова класса Ship -Корабли:')
        print('Класс Ship, наследуется от класса VehicleBase.')
    def set_sail(self):
        print('Создан метод под названием set_sail  свойственный кораблю : Поднять паруса !!!')