TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius():
    try:
        raw = (input("Insert Celcius: "))
        celsius = float(raw)
        if TEMP_MIN <= celsius <= TEMP_MAX:
            print(f"You inserted {celsius} °C")
        else:
            print(f"{celsius} temperature out of range.")

    except ValueError:
        print(f"Could not convert string to float: \'{raw}\'")
    


def main():
    print("Program starting.")
    collectCelsius()
    print("Program ending. ")

if __name__== "__main__":
    main()