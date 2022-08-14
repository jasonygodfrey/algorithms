class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.carTypes = {}
        self.carTypes[1]=big
        self.carTypes[2]=medium
        self.carTypes[3]=small
        
        
        

    def addCar(self, carType: int) -> bool:
        if self.carTypes[carType] > 0:
            self.carTypes[carType]-= 1
            return True
        else:
            return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)