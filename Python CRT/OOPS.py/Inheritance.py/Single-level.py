class Vehicle:
    def __init__(self):
        print("I'm the Vehicle Class Constructor")
    @staticmethod
    def Start():
        print("Vehicle is Started")
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print("I'm the Car Class Constructor")
    @staticmethod
    def Start():
        print("Car is started")
C1=Car()
C1.Start()