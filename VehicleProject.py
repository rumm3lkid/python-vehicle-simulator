
# This program simulates a vehicle dealership where the user can choose to purchase a Truck, Car, or Motorcycle. The program then displays the features of the chosen vehicle, such as ignition, radio, and condition.


class vehicleDealership:

    def vehicleChoice(self, choice):

        if choice == "Truck":
            print("You have purchased a Truck")

        elif choice == "Car":
            print("You have purchased a Car")

        elif choice == "Motorcycle":
            print("You have purchased a Motorcycle")

dealership = vehicleDealership()

print("Welcome to the Vehicle Dealership! Would you like to buy a Truck, Car, or Motorcycle?")
if input("Type 'yes' to continue: ") == "yes":
    vehicleChoice = input("Great! Which vehicle do you want to buy? (Truck, Car, Motorcycle): ")
    dealership.vehicleChoice(vehicleChoice)
else:
    print("Thank you for visiting the Vehicle Dealership. Have a great day!")


class Vehicle:
    def miles(self, miles): 
        print(f"This vehicle has {miles} miles on it")

    def ignition(self, wear):
        if wear >= 25:
            print("Vroom\nIgnition is on")
        else:
            print("Ignition is too worn out to start the engine")

    def radio(self):
        print("Radio tuned and playing music")

    def condition(self, wear):
        if wear >= 25:
            print("Vehicle is in good condition")
        else:
            print("Vehicle is in poor condition")





if vehicleChoice == "Truck":
    Truck = Vehicle()
    Truck.ignition(100)
    Truck.radio()
    Truck.condition(100)

elif vehicleChoice == "Car":
    Car = Vehicle()
    Car.ignition(100)
    Car.radio()
    Car.condition(100)

elif vehicleChoice == "Motorcycle":
    Motorcycle = Vehicle()
    Motorcycle.ignition(100)
    Motorcycle.radio()
    Motorcycle.condition(100)