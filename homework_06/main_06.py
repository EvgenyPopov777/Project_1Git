# # #Исключения
# a =100
# b = '2'
# try:
#     c = a /b
# except :
#     #c = 0
#     print('Ошибка в делении')
#     print('переменная а = ',a,'переменная b = ', b)
# #print('Переменная с =',c)

class Car():#создание класса Car
    def __init__(self,weight,fuel,fuel_cnsuption,started): #Иници-я параметра
        self.weigh = weight #Вес автомобиля типа int
        self.fuel = fuel # Условное количество оставшегося топлива
        self.fuel_cnsuption = fuel_cnsuption # условное значение, сколько
        #едениц топлива расходуется на еденицу расстояния
        self.started = started  # состояние заведён или нет


    def Start(self):
        if self.started == 'старт':
            print('Стартанули.')
            return True

        if self.started != 'старт':## Уровень топлива при условии, что стартанули.
            if self.fuel > 0:
                self.started == True
                print('Чё-то мы не стартанули, давайте проверим уровень топлива: ')
                print('Топливо в порядке, уровень заряда бака = '+str(self.fuel) + '%' + ' машина заведена')
            else:
                print('Завести машину не удалось, т.к топлива  =',self.fuel)

    def move(self,distance):
        self.distance = distance
        desc = distance * self.fuel_cnsuption
        if desc <=self.fuel:
            print('Давайте проверим, хватит ли вам топлива, для дальнейшей поездки:')
            print('Топлива хватает, хорошего дня сэр!')
        elif desc > self.fuel:
            print(' Увы, но топлива на такое расстояние вам не хватит!')

#Проверяем:
my_car = Car(350,50,5,'tстарт')# Если пишем "незаведено мы никуда не поедем"
print(my_car.Start())
my_car.move(10)# Если ввести например 20, то программа нам скажет, топлива не хватит на такое расстояние.




