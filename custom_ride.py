print("Choose your ride: ")
print("\n1. Car")
print("2. Bike")
ride = int(input("Enter your option: "))
if ride == 1:
    print("You have chosen your ride as a car.")
    print("Pick your car type:")
    print("1. Sedan")
    print("2. SUV")
    car_type = int(input("Enter your option: "))
    if car_type == 1:
        print("You have chosen a Sedan.")
        print("\nMax speed: 250 km/h")
        print("Seats: 4 passengar seats, 1 driver seat")
        print("Colour: Black")
        print("Enjoy your ride!")
    elif car_type == 2:
        print("You have chosen a SUV.")
        print("\nMax speed: 300 km/h")
        print("Seats: 6 passengar seats, 1 driver seat")
        print("Colour: White")
        print("Enjoy your ride!")

    else:
        print("You have chosen an invalid input.")
elif ride == 2:
    print("You have chosen your ride as a bike.")
    print("Pick your bike type:")
    print("1. Mountain bike")
    print("2. Activa")
    bike_type = int(input("Enter your option: "))
    if bike_type == 1:
        print("You have chosen a Mountain bike.")
        print("\nMax speed: 275 km/h")
        print("Colour: Grey")
        print("Suitable terrain: Rocky terrain")
        print("Enjoy your ride!")
    elif bike_type == 2:
        print("You have chosen an Activa.")
        print("\nMax speed: 245 km/h")
        print("Colour: Red")
        print("Suitable terrain: Smooth terrain")
        print("Enjoy your ride!")
    else:
        print("You have chosen an invalid input.")
else:
    print("You have chosen an invalid input.")
