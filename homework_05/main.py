class VehicleBase:
    def __init__(self,vehicle_weight):
        self.vehicle_weight = vehicle_weight
        print('Класс VehicleBase, вес трансопртного средства, в кг : ')
        print(vehicle_weight)

class Ship(VehicleBase):
    def __init__(self,vehicle_weight,max_weight):
        super().__init__(vehicle_weight)
        self.max_weight = max_weight
        print('Класс Ship, наследуется от класса VehicleBase, информация о максимальном весе, который можно погрузить в машину в кг(типо): ')
        print(max_weight)

    def set_sail(self):
        print('Создан метод  set_sail, свойственный кораблю : Поднять паруса!!! ')

class Plane(VehicleBase):
    def __init__(self,vehicle_weight,num):
        super().__init__(vehicle_weight)
        self.cargo = num
        print('Текущее состояние cargo (веса) на экземпляре это : ', num)

    def add_cargo(self,num):
        self.cargo += num
        print('После вызова метода add_cargo  значение ' + 'ГРУЗА' + ' на экземпляре должно быть : ' + str(self.cargo))




def main():
    my_ships =Ship(3250,20)
    my_ships.set_sail()# Вывел метод set_sail
    my_plane =Plane(3250,2)#текущее состояние cargo на экземпляре это 2
    my_plane.add_cargo(5)###---то после вызова метода add_cargo на экземпляре с передачей аргумента 5 значение cargo на экземпляре должно быть 7

main()#Вызов функции main











