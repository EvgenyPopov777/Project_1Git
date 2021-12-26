from pydantic import BaseModel
from exceptions import LowFuelError,ValueError
# Родитель
class VehicleBase(BaseModel):
    color:str

#Машина...дочерний
class Car(VehicleBase):
    fuel:int
    started:bool
#Функция включения и выключения машины по топливу....
    def start(self):
        if self.fuel > 0:
            self.started = True
            print('Топливо > 0 и  = '+str(self.fuel)+' Включаем, self.started = ',self.started)
        else:
            raise LowFuelError('Недостаточно топлива')

    def stop(self):
            self.started = False
            print('Выключаем. Значение = ',self.started)
#Груз...дочеринй
class Plan(VehicleBase):
    cargo: int # текущий груз
    max_cargo: int  # максимальный груз
    additional_cargo: int  # добавочный груз
#Функция проверки груза...
    def add_cargo(self):# должно быть так: если текущй груз + добавочный груз <= max.cargo(максимальный груз), то вывести результат иначе вывести исключение вывести исключение
        self.cargo =self.cargo + self.additional_cargo
        if self.cargo < self.max_cargo:
            print('Лимит веса = '+ str(self.max_cargo) + '. Сумма веса = ' + str(self.cargo) + ' и не привышает лимит.')
            print('self.cargo = ',self.cargo)
        else:
            raise ValueError('Превышен лимит груза')
# Функция удаления груза...
    def remove_all_cargo(self):
        # num = self.cargo
        print('обнуляем self.cargo :')
        self.cargo = 0
        return self.cargo
#Основная функция...
def main():
    car =Car(color = 'Red', fuel = 0, started = False)
    print(car)
    car.start()
    plan =Plan(color = 'Red', cargo = 50, max_cargo = 200, additional_cargo=60,)
    print(plan)
    plan.add_cargo()
    print(plan.remove_all_cargo())
    plan.add_cargo()
main()


