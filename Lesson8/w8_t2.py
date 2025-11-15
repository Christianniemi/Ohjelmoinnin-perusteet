import library

def showOptions():
    print("Options:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")
    return None

def askChoice():
    choice = int(input("Your choice:"))
    return choice

def askValue(choise):
    if choise == 1:
        value1 = float(input("Insert first addend value:"))
        value2 = float(input("Insert second addend value:"))
        sum = library.add(value1, value2)
        print(f"{value1} + {value2} = {sum}")

    elif  choise == 2:
        value1 = float(input("Insert minuend value:"))
        value2 = float(input("Insert subtraend value:"))
        sum = library.subtract(value1, value2)
        print(f"{value1} - {value2} = {sum}")
    elif choise == 3:
        value1 = float(input("Insert multiplicand value:"))
        value2 = float(input("Insert multiplier value:"))
        sum = library.multiply(value1, value2)
        print(f"{value1} * {value2} = {sum}")
    elif choise == 4:
        value1 = float(input("Insert dividend value:"))
        value2 = float(input("Insert divisor value:"))
        sum = library.divide(value1, value2)
        print(f"{value1} / {value2} = {sum}")
    elif choise == 0:
        print("Exiting program. ")
    else:
        print("Unknown option.")
    return None
    
    
        

def main():
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()
        if choice ==0:
                print("Exiting program.")
                break
        askValue(choice)
    print("\nProgram ending.")

if __name__ == "__main__":
    main()