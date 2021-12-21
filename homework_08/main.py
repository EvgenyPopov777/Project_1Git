from dataclasses import  dataclass
from pydantic import BaseModel
from exceptions import exceept_1,exceept_2
@dataclass
class VehicleBase(BaseModel):
    pass
    # color: str
    # def cool(self):
    #     pass


@dataclass
class Car():# Единственное, что я не сделал, так это наследование от VehiclaBase у Car и Plane. С ним, вся конструкция рушится.
    started: bool = False

#Функция включения и выключения машины по топливу
    def start(self,fuel:int):
        self.fuel =fuel
        if self.fuel > 0:
            self.started = True
            print('Топливо > 0 и  = '+str(self.fuel)+' Включаем:',self.started)
        else:
            print(exceept_1.fing())

    def stop(self):
            # self.fuel = 0
            self.started = False
            print('Выключаем. Значение = ',self.started)

@dataclass
class Plan():
    cargo: int # текущий груз
    additional_cargo: int  # добавочный груз
    max_cargo: int # максимальный груз

#Функция проверки груза
    def add_cargo(self):# должно быть так: если текущй груз + добавочный груз <= max.cargo(максимальный груз), то вывести результат иначе вывести исключение вывести исключение
        self.cargo =self.cargo + self.additional_cargo
        if self.cargo < self.max_cargo:
            print('Лимит веса = '+ str(self.max_cargo) + '. Сумма веса = ' + str(self.cargo) + ' и не привышает лимит.')
        else:
            print(exceept_2.fin())


    def remove_all_cargo(self):
        num = self.cargo
        self.cargo = 0
        return num


def main():
    car = Car()
    car.start(1)
    # car.stop()
    plan = Plan(50,30,100)#указываем текущий вес, затем добавочный и максимальный вес!
    plan.add_cargo()
    print(plan.remove_all_cargo())


main()