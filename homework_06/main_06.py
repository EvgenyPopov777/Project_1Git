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


    def move(self,distance):#Проверка на нехватку топлива
        self.distance = distance
        desc = distance * self.fuel_cnsuption
        if desc <=self.fuel:
            print('Давайте проверим, хватит ли вам топлива, для дальнейшей поездки:')
            #print('Топлива хватает, хорошего дня сэр!')
            print('Топлива = '+ str(self.fuel)+ ' на  расстояние = ' +str(distance) + ' вам хватит.Хорошего дня сэр!')#конкатенация
        elif desc > self.fuel:
            print(' Увы, но топлива = '+ str(self.fuel)+ ' на  расстояние = ' +str(distance) + ' вам не хватит!')


    def start(self): #Проверка на старт

            if self.started == 'старт' and self.fuel > 0:
                print('Стартанули.')

            if self.started != 'старт':
                print('Чё-то мы не стартанули, давайте проверим уровень топлива: ')
            if self.fuel > 0:
                print('Топливо в порядке, уровень заряда бака = '+str(self.fuel) + '%' + ' машину завели')#если не стартанули смотри есть ли топливо
            try:
                if self.started != 'старт' and self.fuel == 0:# если в условии хотябы одно не истино то ложь
                    #return False
                    #pass
                    print('fsf')
            except LowFuelError :
                print('Неа мы даже не стартанём т.к топлива = 0')# не хочет выводить')





#Проверяем:
my_car = Car(350,0,5,'старт')# Если пишем "незаведено мы никуда не поедем"
my_car.start()
my_car.move(10)# Если ввести например 20, то программа нам скажет, топлива не хватит на такое расстояние.




