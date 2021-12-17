class VehicleBase:
    def __init__(self,vehicle_weight):
        'Информация о весе'
        self.vehicle_weight = vehicle_weight
        print('Класс VehicleBase, информация о текущем  весе:')
class Ship(VehicleBase):
    def __init__(self,max_weight):
        self.max_weight = max_weight
        print('Класс Ship, наследуется от класса VehicleBase, информация о максимальном весе: ')

    def set_sail(self):
        print('Создан метод  set_sail, свойственный кораблю : Поднять паруса!!! ')

class Plane(VehicleBase):
    def __init__(self,num):
        self.cargo = num
        print('Текущее состояние cargo на экземпляре это : ', num)

    def add_cargo(self,num):
        self.cargo += num
        print('После вызова метода add_cargo  значение ' + 'ГРУЗА' + ' на экземпляре должно быть : ' + str(self.cargo))

def main():
    vb = VehicleBase(3)#закинул значение о текущем весе в экземпляр класса. неизменяемое значение нигде не используется
    print(vb.vehicle_weight)

    my_ships =Ship(17)#неизменяемое значение нигде не используется
    print(my_ships.max_weight)#закинул значение о максимальном весе в экземпляр класса
    print(my_ships.set_sail())# Вывел метод set_sail

    my_plane =Plane(2)#текущее состояние cargo на экземпляре это 2
    my_plane.add_cargo(5)###---то после вызова метода add_cargo на экземпляре с передачей аргумента 5 значение cargo на экземпляре должно быть 7

if __name__ == '__main__':
    main()

main()#Вызов функции main











