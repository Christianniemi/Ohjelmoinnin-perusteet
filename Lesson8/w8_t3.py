def showOptions():
    
    print("Options: ")
    print("1 - Read values")
    print("2 - Amount of values")        
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")
    return None

def askchoice():
    choice = int(input("Your choice: "))
    return choice

def readValues():
    values= []
    filename = input("Insert filename: ")
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            else:
                value = float(line)
                values.append(value)
        
    return values

    

def main():
    print("Program starting.")
    while True:
        showOptions()
        choice = askchoice()
        if choice == 1:
            values = readValues()
            
            print("")
            continue
        
        elif choice == 2:
            values = readValues()
            print(f"Amount of values {len(values)}")
            print("")

        elif choice == 3:
            values = readValues()
            total = sum(values)
            print(f"Sum of values {total:.1f}")
            print("")

        elif choice == 4:
            values = readValues()
            total = sum(values)
            average = total / len(values)
            print(f"Average of values {average:.1f}")
            print("")

        elif choice == 0:
            print("Exiting program. ")
            break
        else:
            print("Unknown option.")
            break
            

if __name__ == "__main__":
    main()