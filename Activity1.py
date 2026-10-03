print("Welcome to Ride Builder")
print("Pick your vehicle")
print("1 for bike")
print("2 for car")
print()

choice=int(input("Enter your choice: 1 or 2: "))
if choice==1:
    print("You have selected bike")
    print("Now choose your bike type 1 for Scooty and 2 for Mountain bike")
    bike_type=int(input("Enter your choice: 1 or 2: "))
    if bike_type==1:
        print("You have selected Scooty")
        print("Top speed is 80km/h")
        print("Best for city roads")
    else :
        print("You have selected Mountain bike")
        print("Top speed is 40km/h")
        print("Best for off roads trails")
elif choice==2:
    print("You have selected car")
    print("Now choose your type of car 1 for Sedan and 2 for SUV")
    car_type=int(input("Enter choice: 1 or 2: "))
    if car_type==1:
        print("You have selected Sedan")
        print("Top speed is 150km/h")
        print("Best for city and humpy roads")
    else:
        print("You have picked SUV")
        print("Top speed is 120km/h")
        print("Best for long drives")

else:
    print("That was not a valid choice.")
    print("Please enter 1 for bike and 2 for car")

print("Custom ride is ready")
print("Enjoy your ride")

