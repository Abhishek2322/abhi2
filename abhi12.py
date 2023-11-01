class Vehicle:
    def __init__(self,mileage,cost):
       self.mileage=mileage
       self.cost=cost
       
    def show_details(self):
        print("i have a vehicle")
        print("the mileage of my vehicle is ",self.mileage)
        print("the cost of my vehicle is",self.cost)
        
c=Vehicle(1000,10000)
c.show_details()
 
class car(Vehicle):
    def show_car(self):
        print("i am a car")
c1=car(200,1200)
c1.show_car()
c1.show_details()
    