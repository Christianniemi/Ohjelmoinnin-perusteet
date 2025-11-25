########################################################
# Task A9_t2
# Developer Christian Niemi
# Date 15.11.2025
########################################################
import sys


def main():
    print("Program starting. ")
    value = int(input("Insert exit code(0-255): "))
    if value == 0:
        sys.exit("Clear exit.")
    else:
        sys.exit("Error code")
    


    

if __name__ == "__main__":
    main()