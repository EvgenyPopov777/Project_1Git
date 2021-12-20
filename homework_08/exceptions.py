from dataclasses import  dataclass
@dataclass
class exceept_1:
    def fing():
        raise Exception('LowFuelError -Недостаточно топлива')

@dataclass
class exceept_2:
    def fin():
        raise ValueError('Перегрузка. Машина не расчитана на такой вес')

