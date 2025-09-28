print("Program starting.")
print("Welcome to the unit converter program! ")
print("Follow the menu instructions below. ")
print("\nOptions: ")

print("1 - Length")
print("2 - Weigth ")
print("0 - Exit ")

Choice1 = int(input("Your choice: "))

if (Choice1 == 1):
    print("\nLength options: ")
    print("1 - Meters to kilometers ")
    print("2 - Kilometers to meters ")
    print("0 - Exit" )
    Choice2 = int(input("Your choice: "))
    if (Choice2 == 1):
        Meters = float(input("Insert meters: "))
        Kilometers = Meters / 1000
        print(f"{round(Meters, 1)} m is {round(Kilometers, 1)} km ")
    if (Choice2 == 2):
        Kilometers = float(input("Insert kilometers: "))
        Meters = Kilometers * 1000
        print(f"{round(Kilometers, 1)} km is {round(Meters, 1)} m ")
    elif (Choice2 == 0):
        print("Exiting...")
    else:
        print("Unknown option. ")
elif (Choice1 == 2):
    print("\nWeight options: ")
    print("1 - Grams to pounds ")
    print("2 - Pounds to grams ")
    print("0 - Exit" )
    Choice2 = int(input("Your choice: "))
    if (Choice2 == 1):
        Grams = float(input("Insert grams: "))
        Pounds = Grams / 453.592
        print(f"{round(Grams, 1)} g is {round(Pounds, 1)} lb ")
    if (Choice2 == 2):
        Pounds = float(input("Insert pounds: "))
        Grams = Pounds * 453.592
        print(f"{round(Pounds, 1)} lb is {round(Grams, 1)} g ")
    elif (Choice2 == 0):
        print("Exiting...")
    else:
        print("Unknown option. ")
elif (Choice1 == 0):
    print("\nExiting...")
else:
    print("\nUnknown option. ")

print("\nProgram ending. ")        
    