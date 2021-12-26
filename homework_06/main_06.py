class Car():#создание класса Car
    def __init__(self,distance,fuel_consuption:int): #Иници-я параметра
        self.weigh = int #Вес автомобиля типа int
        self.started = True # состояние заведён или нет #Если выставит в True то сразу переходит в блок move
        self.fuel_cnsuption = fuel_consuption  # условное значение, сколько
        self.distance =distance
        # едениц топлива расходуется на еденицу расстояния

    def start(self,fuel: int): #Проверка на старт
        self.fuel = fuel  # Условное количество оставшегося топлива
        if not self.started:
            if self.fuel > 0:
                self.started = True
                print('Не started. Включаем:', str(self.started) +'. Топливо > 0 и  = ' + str(self.fuel))
            else:
                raise LowFuelError("Ещё не стартанули и топлива = 0")


    def move(self):#Проверка на нехватку топлива
        print('Давайте проверим, хватит ли вам топлива, для дальнейшей поездки:')
        desc = self.distance * self.fuel_cnsuption
        if desc <= self.fuel:
            print('Топлива = ' + str(self.fuel) + ' на  расстояние = ' + str(self.distance) + ' вам хватит.Хорошего дня сэр!')  # конкатенация
            self.fuel -=desc
            print('Топлива осталось: ',self.fuel)
        else:
            raise NotEnoughFuel("Увы, но топлива на такое расстояние вам не хватит.")


class LowFuelError(Exception):
    pass

class NotEnoughFuel(Exception):
    pass


car = Car(2,3) # расстояние = 10, а расход = 5, соответственно у нас хватит топлива и топливо будет равно 0
car.start(10)# топливо =50
car.move()
# car.move()














