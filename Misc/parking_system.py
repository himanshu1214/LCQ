class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.car_map = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if carType in self.car_map and self.car_map[carType]>0:
            self.car_map[carType] -= 1
            return True
        return False
