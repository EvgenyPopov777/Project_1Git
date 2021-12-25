class Car(Exception):#создание класса Car
    def __init__(self,distance,fuel_consuption:int): #Иници-я параметра
        self.weigh = int #Вес автомобиля типа int
        self.started = False # состояние заведён или нет
        self.fuel_cnsuption = fuel_consuption  # условное значение, сколько
        self.distance =distance
        # едениц топлива расходуется на еденицу расстояния

    def start(self,fuel: int): #Проверка на старт
        self.fuel = fuel  # Условное количество оставшегося топлива
        if self.started == False:
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
            desc = desc -self.fuel
            print('Топлива осталось: ',desc)
        elif desc > self.fuel:
            raise NotEnoughFuel("Увы, но топлива на такое расстояние вам не хватит.")
            # print('Увы, но топлива = '+ str(self.fuel)+ ' на  расстояние = ' +str(self.distance) + ' вам не хватит!')


class LowFuelError(Exception):
    pass

class NotEnoughFuel(Exception):
    pass


car = Car(10,5) # расстояние = 10, а расход = 5, соответственно у нас хватит топлива и топливо будет равно 0
car.start(50)# топливо =50
car.move()











