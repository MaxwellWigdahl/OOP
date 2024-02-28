import CarClass as cc

year_model = int(input("Please input the year your car was made: "))
make = input("Please input the make of your car: ")

my_car = cc.Car(year_model, make)

print("Accelerating")
for i in range(5):
    my_car.accelerate()
    print("Current Speed: ", my_car.get_speed())

print()

print("Breaking")
for i in range(5):
    my_car.brake()
    print("Current Speed: ", my_car.get_speed())