print("Program starting. \n")
print("Options: ")
print("1 - Celcius to Fahrenheit ")
print("2 - Fahrenheit to Celcius ")
print("0 - Exit")
Choice = int(input("Your choice: "))

 
if (Choice == 1):
    Celsius = float(input("Insert the amount of Celcius: "))
    Fahrenheit = Celsius * 1.8 + 32
    print(f"{round(Celsius,1)} °C equals to {round(Fahrenheit,1)} °F ")
elif (Choice == 2):
    Fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    Celsius = (Fahrenheit - 32) / 1.8 
    print(f"{round(Fahrenheit,1)} °F equals to {round(Celsius,1)} °C ")
elif (Choice == 0):
    print("Exiting...")
else:
    print("Unknown option.")
print("\nProgram ending. ")


