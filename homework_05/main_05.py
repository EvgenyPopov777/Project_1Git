class VehicleBase:
    def __init__(self,vehicle_weight):
        'Информация о весе'
        self.vehicle_weight =vehicle_weight
        print('Класс VehicleBase, информация о весе:')
class Ship(VehicleBase):
    def __init__(self,max_weight):
        self.max_weight = max_weight
        print('Класс Ship, наследуется от класса VehicleBase, информация о  максимальном весе:')

    def set_sail(self):
        print('Создан метод под названием set_sail  свойственный кораблю : ')
        print('Поднять паруса')

class Plane(VehicleBase):
    def __init__(self,cargo):
        self.cargo = 0

    def result(self):
        print('После вызова метода add_cargo  значение ' + 'ГРУЗА'+ ' на экземпляре должно быть : ' + str(self.cargo))

    def update(self, num):
            self.cargo = num
            print('Текущее состояние cargo на экземпляре это : ')

    def add_cargo(self,num):
        self.cargo += num

    def main(self):
        vb =VehicleBase(4)
        print(vb.vehicle_weight)
        my_ships =Ship(17)
        print(my_ships.max_weight)
        Sail =Ship.set_sail('')

        my_plane =Plane('')
        my_plane.update(2)###----если текущее состояние cargo на экземпляре это 2
        my_plane.add_cargo(5)###---то после вызова метода add_cargo на экземпляре с передачей аргумента 5 значение cargo на экземпляре должно быть 7
        my_plane.result()

mains =Plane('')
#просто закинул всё в функцию при вызове  создаёт экземпляр класса Ship и Plane и добавляет груз методом add_cargo
mains.main()












