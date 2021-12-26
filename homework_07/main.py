from models.vehiclebase  import VehicleBase
from models.ship import Ship
from models.car import Car


def main():
   VehicleBase()
   ship = Ship()
   ship.set_sail()
   car = Car(10,5)  # расстояние = 10, а расход = 5, соответственно у нас хватит топлива и топливо будет равно 0
   car.start(50)  # топливо =50
   car.move()
if __name__ =='main':
    main()

main()