import sys
from A10_TLib import readValues, displayValues, mergeSort
from A10_TLib import plotNumbers

def main() -> None:
    # Initialize
    Values: list[int] = []
    Filename = ""

    print("Program starting.")

   
    if (len(sys.argv) == 2):
        Filename = sys.argv[1]
        print("The filename '{}' was passed via CLI.".format(Filename))
    else:
        Filename = input("Insert filename: ")
    readValues(Filename, Values)
    # plotNumbers(Values, Filename.split('.')[0] + "_raw")
    # plotNumbers(Values, Filename.split('.')[0] + "_sorted")
    print("Raw '{}' -> ".format(Filename), end='')
    displayValues(Values, Horisontally=True)
    mergeSort(Values)
    print("Ascending '{}' -> ".format(Filename), end='')
    displayValues(Values, True)
    mergeSort(Values, PAsc=False) # Sort in DESCending order
    print("Descending '{}' -> ".format(Filename), end='')
    displayValues(Values, True)
    plotNumbers(Values, Filename.split('.')[0], True)
    # 3. Cleanup
    print("Program ending.")
    Values.clear()
    return None