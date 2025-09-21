print("Calculate fuel comsumption.")
distance = int(input("Enter travel distance(kilometers): "))
usage = int(input("Enter fuel usage(liters): "))
consumption = distance / usage
print("Fuel consumption is", consumption,"l per 100km")