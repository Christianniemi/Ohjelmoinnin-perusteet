########################################################
# Task A9_t1
# Developer Christian Niemi
# Date 15.11.2025
########################################################

def askValue():
    values = []
    while True:
        
        raw = input("Insert floating-point value (0 to stop): ")
        try:
            value = float(raw)
            if value == 0:
                break
        except ValueError:
            print(f"Error! '{raw}' couldn't be converted to float.")
        values.append(value)
    return values

def analyseValues(Pvalues):
    total = sum(Pvalues)
    return total


def main():
    print("Program starting. \n")
    values = askValue()
    total = analyseValues(values)
    print(f"\nFinal sum is {total:.2f}")
    print("Program ending. ")

if __name__ == "__main__":
    main()