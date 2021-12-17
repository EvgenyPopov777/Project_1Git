class Car():#создание класса Car
    def __init__(self,weight,fuel,fuel_cnsuption,started): #Иници-я параметра
        self.weigh = weight #Вес автомобиля типа int
        self.fuel = fuel # Условное количество оставшегося топлива
        self.fuel_cnsuption = fuel_cnsuption # условное значение, сколько
        #едениц топлива расходуется на еденицу расстояния
        self.started = started  # состояние заведён или нет

    def move(self,distance):#Проверка на нехватку топлива
        self.distance = distance
        desc = distance * self.fuel_cnsuption
        if desc <=self.fuel:
            print('Давайте проверим, хватит ли вам топлива, для дальнейшей поездки:')
            print('Топлива = '+ str(self.fuel)+ ' на  расстояние = ' +str(distance) + ' вам хватит.Хорошего дня сэр!')#конкатенация
        elif desc > self.fuel:
            print(' Увы, но топлива = '+ str(self.fuel)+ ' на  расстояние = ' +str(distance) + ' вам не хватит!')

    def start(self): #Проверка на старт

            if self.started == 'старт' :
                print('Стартанули.')

            if self.started != 'старт':
                print('Чё-то мы не стартанули, давайте проверим уровень топлива: ')
            if self.fuel > 0:
                print('Топливо в порядке, уровень заряда бака = '+str(self.fuel) + '%' + ' машину завели')#если не стартанули смотри есть ли топливо
            if self.started != 'старт' and self.fuel == 0:# если в условии хотябы одно не истино то ложь
                class LowFuelError(Exception):
                    print('Ещё не стартанули и  топлива = 0')
                    raise LowFuelError('')