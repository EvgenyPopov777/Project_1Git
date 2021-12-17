from models.vehiclebase  import VehicleBase
from models.ship import Ship
from models.car import Car
from  exceptions import Exceptions


def main():
   vehiclebase = VehicleBase
   print(vehiclebase)
   print('Пример вызова класса Ship -Корабли:')
   ship =Ship()
   ship.set_sail()
   print('Пример вызова класса Car -Машины:')
   my_car = Car(350, 5, 5, 'старт')  # Инициализация экземпляров класса.
   my_car.start()   #Демонстрация вызова метода
   my_car.move(10)
   print('Еденица расстояния топлива по отношению к пути :',my_car.fuel_cnsuption) #Пример обращения к атрибуту класса
   print('Пример вызова класса Exceptions - Исключение:')# отдельный пример.
   room = Exceptions
   room.get_room_number()
if __name__ =='main':
    main()

main()